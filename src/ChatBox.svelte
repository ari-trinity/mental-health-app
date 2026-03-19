<script>
  // ===========================
  // BRAIN SECTION - AI Chatbot!
  // ===========================

  import { createEventDispatcher } from 'svelte';
  import { onMount, tick } from 'svelte';

  const dispatch = createEventDispatcher();

  export let userName = "";  // get user's name

  // extract just the first name
  $: firstName = userName ? userName.trim().split(/\s+/)[0] : '';

  let messages = [];
  let inputMessage = '';
  let isTyping = false;
  let suggestions = [];
  let messagesContainer;

  // pick a random item from an array
  function pick(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  }

  // scroll to the bottom of the messages container
  async function scrollToBottom() {
    await tick();
    if (messagesContainer) {
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
  }

  // =========================================================
  // RESPONSE DATABASE — keywords, multiple replies, follow-ups
  // =========================================================
  const responseDatabase = [
    {
      keywords: ['crisis', 'hurt myself', 'end it', 'suicide', 'kill myself', 'self-harm', 'self harm', 'don\'t want to live', 'no reason to live', 'want to die'],
      responses: [
        "I'm really concerned about what you're sharing, and I want you to know that you matter. Please reach out to the **988 Suicide & Crisis Lifeline** by calling or texting **988** — they're available 24/7. You can also text HOME to **741741** to reach the Crisis Text Line. You are not alone.",
        "What you're going through sounds incredibly painful, and I'm glad you told me. Please contact the **988 Suicide & Crisis Lifeline** right now — call or text **988**. If you're in immediate danger, please call **911**. There are people who want to help you.",
        "I hear you, and I take what you're saying seriously. Your life has value. Please reach out to a crisis counselor right now: call or text **988**, or text HOME to **741741**. They are trained to help and available 24/7."
      ],
      followUps: ["Tell me more about what you're feeling", "What crisis resources are available?", "I need help right now"]
    },
    {
      keywords: ['anxious', 'anxiety', 'worried', 'nervous', 'panic', 'panicking', 'panic attack', 'racing thoughts', 'can\'t breathe', 'overwhelmed', 'on edge'],
      responses: [
        "I hear that you're feeling anxious, and that takes courage to share. Anxiety can feel overwhelming, but remember — it's temporary. Let's try something: take a slow breath in for 4 counts, hold for 4, and breathe out for 6. Would you like to try a full guided breathing exercise?",
        "Anxiety can be really tough. One thing that often helps is grounding: name **5 things you can see**, **4 you can touch**, **3 you can hear**, **2 you can smell**, and **1 you can taste**. This can help bring you back to the present moment. Would you like to talk about what's causing your worry?",
        "It sounds like anxiety is weighing on you right now. That's completely valid. Some things that can help include deep breathing, progressive muscle relaxation, or simply talking through what's on your mind. What feels right for you?",
        "Racing thoughts and worry can feel exhausting. You're not alone in this. Try placing your hand on your chest and taking three slow, deep breaths. Sometimes physically feeling your heartbeat slow down can be really grounding. What's on your mind today?"
      ],
      followUps: ["Guide me through a breathing exercise", "I want to talk about what's worrying me", "What are some coping strategies for anxiety?", "I'm having a panic attack"]
    },
    {
      keywords: ['sad', 'depressed', 'depression', 'down', 'hopeless', 'empty', 'numb', 'crying', 'tears', 'miserable', 'despair'],
      responses: [
        "I'm sorry you're going through this. Feeling sad or depressed can be incredibly heavy, and it's okay to not be okay right now. Your feelings are valid. Sometimes it helps to do one small kind thing for yourself — like getting a glass of water, stepping outside for a minute, or wrapping yourself in a blanket. What sounds manageable right now?",
        "Depression can make everything feel gray and exhausting. I want you to know that reaching out like this is a strength, not a weakness. You don't have to have it all figured out. Would you like to talk about what's been going on, or would you prefer some gentle affirmations?",
        "I hear you, and I'm here for you. When sadness feels this deep, even small steps matter. Have you been able to eat today? Get some rest? Sometimes taking care of the basics is the bravest thing we can do. What would feel supportive right now?",
        "Your pain is real, and you deserve support. Depression often lies to us — it says things will never get better, but that isn't true. Recovery isn't linear, and asking for help is a sign of strength. Would you like to explore some coping strategies together?"
      ],
      followUps: ["Share some affirmations with me", "What are signs I should see a professional?", "Help me with small steps I can take today", "I just need someone to listen"]
    },
    {
      keywords: ['stressed', 'stress', 'pressure', 'burned out', 'burnout', 'burnt out', 'overworked', 'too much', 'can\'t handle', 'falling apart'],
      responses: [
        "It sounds like you're carrying a lot right now. Stress can build up until it feels unbearable, but you don't have to tackle everything at once. Try this: write down everything on your mind, then circle just ONE thing you can address today. Giving yourself permission to focus small can bring big relief.",
        "Burnout is real, and it's your mind and body telling you that something needs to change. Have you been able to take any breaks recently? Even 5 minutes of stepping away — no phone, no tasks — can help reset your nervous system.",
        "When stress piles up, it can feel like you're drowning. Let's take a step back together. What's the single biggest source of stress right now? Sometimes naming it specifically can make it feel more manageable.",
        "You're dealing with a lot, and I want to acknowledge that. Chronic stress affects your sleep, your mood, and even your physical health. It's okay to set boundaries and say no to things. What would it look like to take one thing off your plate this week?"
      ],
      followUps: ["Help me prioritize what to tackle first", "How can I set better boundaries?", "I need a quick stress relief technique", "Tell me about burnout recovery"]
    },
    {
      keywords: ['sleep', 'insomnia', 'can\'t sleep', 'tired', 'exhausted', 'fatigue', 'nightmares', 'restless', 'tossing and turning'],
      responses: [
        "Sleep struggles are incredibly frustrating and affect everything else in your life. Here are some things that can help: try keeping a consistent bedtime, avoid screens 30 minutes before bed, and keep your room cool and dark. A simple body scan meditation can also work wonders. Would you like me to walk you through one?",
        "Being exhausted but unable to sleep is one of the most frustrating cycles. One technique that helps many people is the **4-7-8 breathing method**: breathe in for 4 seconds, hold for 7, and exhale slowly for 8. It activates your body's relaxation response. Have you tried any sleep routines before?",
        "Lack of sleep can make everything feel harder — your emotions, your focus, your patience. You're not alone in this. Some things worth trying: journaling before bed to 'download' your thoughts, limiting caffeine after 2 PM, and creating a calming pre-sleep ritual. What does your current bedtime routine look like?",
        "Nightmares and restless sleep can be signs that your mind is processing difficult emotions. That's actually normal, even if it's unpleasant. If sleep issues persist for more than a few weeks, it may be worth talking to a healthcare provider. In the meantime, would you like some relaxation techniques?"
      ],
      followUps: ["Walk me through a body scan meditation", "What is sleep hygiene?", "I keep having nightmares", "How does sleep affect mental health?"]
    },
    {
      keywords: ['lonely', 'alone', 'isolated', 'no friends', 'nobody cares', 'disconnected', 'left out', 'abandoned'],
      responses: [
        "Feeling lonely is one of the most painful human experiences, and I'm sorry you're going through it. Even when it feels like nobody understands, please know that reaching out here is a meaningful step. Connection can start small — even a brief interaction with a neighbor or a message to an old friend counts.",
        "Loneliness can feel like an invisible weight. It doesn't mean something is wrong with you — it means you're human and you need connection. Sometimes the first step is the hardest. Is there one person you could reach out to today, even with just a 'thinking of you' text?",
        "I hear you, and your feelings of isolation are valid. Many people feel this way, even if they don't show it. Building connection takes time, but it can start with small steps: joining an online community, volunteering, or even starting conversations in daily life. What feels approachable to you?",
        "Being alone and feeling lonely are different things, and both are hard. You deserve meaningful connections. Sometimes loneliness is also a signal that we need to reconnect with ourselves first. Have you tried journaling, spending time in nature, or doing something creative?"
      ],
      followUps: ["How can I build new connections?", "I feel like nobody understands me", "What are some ways to feel less isolated?", "Tell me about online support communities"]
    },
    {
      keywords: ['angry', 'anger', 'furious', 'frustrated', 'rage', 'irritated', 'mad', 'pissed', 'annoyed', 'resentful'],
      responses: [
        "Anger is a valid emotion — it often shows up when our boundaries have been crossed or when something feels unfair. The goal isn't to suppress it, but to express it in healthy ways. One quick technique: clench your fists tight for 5 seconds, then release. Notice the difference. Would you like to talk about what's making you angry?",
        "It sounds like you're really frustrated right now. Anger often masks deeper feelings like hurt, fear, or disappointment. When you're ready, it can help to ask yourself: 'What am I really feeling underneath this anger?' There's no rush — take your time.",
        "Feeling angry is completely human. Some healthy ways to process it include physical activity (even a brisk walk), writing an uncensored letter you don't send, or speaking your feelings out loud. What usually helps you when you're feeling this way?",
        "I can sense your frustration, and I want you to know it's okay to feel this way. Anger becomes a problem only when we act on it in harmful ways. Right now, try taking three slow, deep breaths before we continue. What's going on?"
      ],
      followUps: ["Help me calm down right now", "I want to understand why I'm so angry", "What are healthy ways to express anger?", "How do I stop snapping at people?"]
    },
    {
      keywords: ['work', 'job', 'boss', 'coworker', 'career', 'office', 'workplace', 'fired', 'laid off', 'unemployment', 'hate my job'],
      responses: [
        "Work-related stress is one of the most common sources of mental strain. Whether it's a difficult boss, heavy workload, or feeling unfulfilled, those feelings deserve attention. What aspect of work is weighing on you the most right now?",
        "Spending so much of our lives at work means that when things aren't going well there, it affects everything. It's okay to feel frustrated or drained. Have you been able to set any boundaries between work and personal time? Even small ones can make a difference.",
        "Career stress can feel all-consuming. Remember: your job is something you do, not who you are. Your worth isn't measured by productivity. What would it look like to take one step toward improving your work situation this week?",
        "Whether you're dealing with a toxic environment, job loss, or career uncertainty — that's genuinely stressful. Give yourself permission to feel whatever you're feeling without judgment. Would you like to talk through what's happening?"
      ],
      followUps: ["How do I deal with a toxic workplace?", "I'm thinking about changing careers", "Help me set work-life boundaries", "I'm dealing with job loss"]
    },
    {
      keywords: ['relationship', 'partner', 'boyfriend', 'girlfriend', 'spouse', 'marriage', 'breakup', 'break up', 'divorce', 'dating', 'heartbreak', 'heartbroken'],
      responses: [
        "Relationships are such an important part of our lives, and when they're struggling, it can affect everything. Whether you're going through a rough patch or a breakup, your feelings are completely valid. Would you like to talk about what's happening?",
        "Heartbreak and relationship stress can feel physically painful — that's not just in your head. Your brain processes emotional and physical pain similarly. Be gentle with yourself right now. What do you need most in this moment?",
        "Relationship difficulties are some of the hardest things to navigate. Communication, boundaries, and self-care are all important pieces of the puzzle. What part of your relationship situation is weighing on you the most?",
        "Whether it's a new relationship, a long-term partnership, or the aftermath of one ending, these feelings matter. You deserve to be in relationships where you feel valued and respected. What's on your mind?"
      ],
      followUps: ["I'm going through a breakup", "How do I communicate better with my partner?", "What does a healthy relationship look like?", "I'm struggling to move on"]
    },
    {
      keywords: ['self-esteem', 'self esteem', 'confidence', 'worthless', 'not good enough', 'ugly', 'hate myself', 'self-worth', 'insecure', 'imposter', 'inadequate', 'failure', 'loser'],
      responses: [
        "I'm sorry you're feeling this way about yourself. The inner critic can be incredibly loud and convincing, but it's not telling you the truth. Try this: think of something you'd say to a friend feeling this way. Now say that to yourself. You deserve the same compassion.",
        "Low self-esteem often comes from internalizing messages we received growing up or comparing ourselves to others. But here's the truth: you are enough, exactly as you are right now. Growth is wonderful, but it should come from self-love, not self-hate.",
        "Imposter syndrome and feelings of inadequacy are incredibly common — even the most successful people experience them. The fact that you care about doing well shows your dedication. What specific thoughts are coming up for you?",
        "Negative self-talk is like a bad habit — it takes time and practice to change. One powerful technique is to notice when you're being critical, pause, and rephrase the thought with kindness. For example, 'I'm such a failure' becomes 'I'm learning and growing.' What negative thoughts have been loudest lately?"
      ],
      followUps: ["Help me challenge negative self-talk", "How do I build self-confidence?", "I keep comparing myself to others", "Share some self-compassion exercises"]
    },
    {
      keywords: ['motivation', 'unmotivated', 'lazy', 'procrastinating', 'stuck', 'can\'t focus', 'no energy', 'don\'t care', 'apathetic', 'what\'s the point'],
      responses: [
        "Lack of motivation is often not about being 'lazy' — it can be a sign of burnout, depression, or simply needing rest. Be kind to yourself. Sometimes the smallest action — like making your bed or going for a 5-minute walk — can create momentum. What's one tiny thing you could do right now?",
        "Feeling stuck is frustrating, but it doesn't mean you're failing. Sometimes we need to rest before we can move forward. Give yourself permission to take a break without guilt. When you're ready, try the **2-minute rule**: if something takes less than 2 minutes, do it now.",
        "When everything feels pointless, it might help to reconnect with your 'why.' What matters to you? What did you used to enjoy? Sometimes motivation returns when we stop forcing it and start with curiosity instead. Is there anything that used to bring you joy?",
        "Procrastination often comes from perfectionism or fear of failure, not laziness. Try breaking tasks into ridiculously small steps — so small they feel almost silly. 'Open the document' instead of 'Write the report.' Small wins build momentum."
      ],
      followUps: ["Help me break a task into small steps", "I think I might be depressed", "How do I stop procrastinating?", "I've lost interest in things I used to enjoy"]
    },
    {
      keywords: ['grateful', 'gratitude', 'thankful', 'blessed', 'appreciate', 'fortunate'],
      responses: [
        "That's beautiful! 🌿 Gratitude is one of the most powerful tools for mental wellness. Studies show that regularly practicing gratitude can rewire your brain to notice more positive things. What are three things you're grateful for right now?",
        "I love that you're in a space of gratitude! 🌟 Appreciating what we have — even the small things — can shift our entire perspective. Have you tried keeping a gratitude journal? Writing down 3 things each night can be transformative.",
        "Gratitude is such a healing practice. Whether you're thankful for big things or tiny moments, it all counts. Some people find it helpful to share their gratitude with others — it strengthens connections too. What's bringing you gratitude today?"
      ],
      followUps: ["How do I start a gratitude journal?", "Tell me more about gratitude's benefits", "I want to be more mindful", "What are other positive habits I can build?"]
    },
    {
      keywords: ['happy', 'good', 'great', 'wonderful', 'amazing', 'fantastic', 'excited', 'joyful', 'content', 'peaceful', 'better', 'improving'],
      responses: [
        "That's wonderful to hear! 🌟 I'm genuinely glad you're feeling good. Positive moments matter, and it's important to savor them. What's been contributing to these good feelings? Reflecting on that can help you create more of these moments.",
        "That makes me so happy to hear! 🎉 When things are going well, try to take a mental snapshot — really absorb how this feels. On harder days, you can look back and remember that good times do come. What's been going well for you?",
        "I love that! 😊 Celebrating the good moments is just as important as working through the hard ones. You deserve to feel joy. Is there anything specific that's been lifting your spirits?",
        "That's amazing! Your positive energy is wonderful. This is a great time to invest in habits that support your wellbeing — so when harder times come, you have a strong foundation. What brings you the most joy in your daily life?"
      ],
      followUps: ["How can I maintain this positive feeling?", "I want to build healthy habits", "Tell me about mindfulness", "How can I spread positivity to others?"]
    },
    {
      keywords: ['hello', 'hi', 'hey', 'greetings', 'what\'s up', 'good morning', 'good evening', 'good afternoon'],
      responses: [
        firstName
          ? `Hello ${firstName}! 😊 I'm your wellness companion, and I'm here to support you in whatever way you need. We can talk about how you're feeling, explore coping strategies, practice mindfulness, or just chat. What would you like to focus on today?`
          : "Hello! 😊 I'm your wellness companion, and I'm here to support you in whatever way you need. We can talk about how you're feeling, explore coping strategies, practice mindfulness, or just chat. What would you like to focus on today?",
        firstName
          ? `Hi ${firstName}! Great to see you here. How are you doing today? I'm ready to listen, share resources, or just be a supportive presence — whatever you need.`
          : "Hi there! Great to see you here. How are you doing today? I'm ready to listen, share resources, or just be a supportive presence — whatever you need."
      ],
      followUps: ["How are you doing?", "I need someone to talk to", "What can you help me with?", "I'm feeling stressed"]
    },
    {
      keywords: ['thank', 'thanks', 'appreciate it', 'helpful'],
      responses: [
        "You're very welcome! 💙 I'm always here whenever you need support. Remember, showing up for yourself — like you did today — is a powerful act of self-care.",
        "I'm glad I could help! Taking time for your mental health is one of the most important things you can do. Don't hesitate to come back anytime you need a safe space to talk.",
        "You're so welcome! 🌿 It means a lot that you feel comfortable sharing here. Keep being kind to yourself — you're doing better than you think."
      ],
      followUps: ["I'd like to talk about something else", "Any daily wellness tips?", "Can you share an affirmation?", "How can I help others who are struggling?"]
    },
    {
      keywords: ['breathing', 'breathe', 'breathing exercise', 'calm down', 'relax', 'relaxation', 'meditation', 'meditate'],
      responses: [
        "Let's do a breathing exercise together! 🌬️\n\n**Box Breathing (4-4-4-4):**\n1. Breathe in slowly for **4 seconds**\n2. Hold your breath for **4 seconds**\n3. Breathe out slowly for **4 seconds**\n4. Hold empty for **4 seconds**\n\nRepeat this 4 times. This technique is used by Navy SEALs to stay calm under pressure. How do you feel after trying it?",
        "Here's a simple relaxation technique you can try right now:\n\n**Progressive Muscle Relaxation:**\n1. Start with your toes — tense them for 5 seconds, then release\n2. Move to your calves, thighs, stomach, hands, arms, shoulders, and face\n3. Tense each group for 5 seconds, then let go completely\n4. Notice the difference between tension and relaxation\n\nThis helps your body physically release stress. Would you like to try it?",
        "Great that you want to practice mindfulness! Here's a quick grounding meditation:\n\n**5-4-3-2-1 Grounding:**\n- **5** things you can SEE\n- **4** things you can TOUCH\n- **3** things you can HEAR\n- **2** things you can SMELL\n- **1** thing you can TASTE\n\nTake your time with each one. This brings you into the present moment and calms anxious thoughts."
      ],
      followUps: ["That helped, what else can I try?", "Tell me about meditation apps", "I want to build a daily mindfulness practice", "How does breathing help with anxiety?"]
    },
    {
      keywords: ['affirmation', 'affirmations', 'positive', 'encourage', 'encouragement', 'inspire', 'mantra'],
      responses: [
        "Here are some affirmations for you today 🌿:\n\n• I am worthy of love and respect, exactly as I am\n• My feelings are valid, and it's okay to feel them\n• I am stronger than I realize\n• Today, I choose progress over perfection\n• I deserve rest without guilt\n\nTry saying one of these out loud or writing it somewhere you'll see it. Which one resonates most with you?",
        "Sometimes we need to hear the things we forget to tell ourselves:\n\n• I am doing the best I can, and that is enough\n• Difficult times are temporary; my strength is permanent\n• I am allowed to take up space in this world\n• My past does not define my future\n• I am growing, even when I can't see it\n\nRepetition is key — the more you say these, the more you'll believe them. 💙",
        "Here's a powerful affirmation practice:\n\nLook at yourself in the mirror and say:\n*\"I see you. I accept you. I am proud of you.\"*\n\nIt might feel awkward at first — that's completely normal. Over time, this practice can genuinely change how you relate to yourself. Would you like affirmations for a specific area of your life?"
      ],
      followUps: ["Give me affirmations for self-confidence", "How do affirmations work scientifically?", "I find it hard to believe positive things about myself", "What other positive practices can I try?"]
    },
    {
      keywords: ['help', 'what can you do', 'how do you work', 'features', 'options', 'what do you offer'],
      responses: [
        "I'm here to support your mental wellness in several ways! Here's what I can help with:\n\n🧘 **Guided exercises** — Breathing, meditation, grounding, and relaxation techniques\n💬 **Emotional support** — A safe space to talk about anxiety, sadness, stress, anger, loneliness, and more\n🌟 **Affirmations & encouragement** — Positive reminders when you need a boost\n📚 **Coping strategies** — Practical tools for managing difficult emotions\n🆘 **Crisis resources** — Immediate help and hotline numbers when you need them\n❤️ **Self-care guidance** — Tips for sleep, relationships, self-esteem, and daily wellness\n\nWhat would you like to explore?",
      ],
      followUps: ["I'm feeling anxious", "Guide me through a breathing exercise", "I need some encouragement", "Tell me about coping strategies"]
    },
    {
      keywords: ['family', 'parent', 'parents', 'mom', 'dad', 'mother', 'father', 'sibling', 'brother', 'sister', 'child', 'children', 'kids'],
      responses: [
        "Family relationships can be some of the most complex and emotionally charged parts of our lives. Whether it's conflict, distance, or complicated dynamics, those feelings run deep. Would you like to share more about what's going on with your family?",
        "Family situations can bring up so many emotions — love, frustration, guilt, sadness, and everything in between. Whatever you're experiencing is valid. Sometimes it helps to focus on what you can control: your own boundaries and responses. What's been happening?",
        "Our families shape us in profound ways, and navigating those relationships as we grow can be really challenging. Whether you're dealing with a specific conflict or a more general feeling, I'm here to listen without judgment."
      ],
      followUps: ["How do I set boundaries with family?", "I'm dealing with family conflict", "I feel guilty about my family situation", "How do I cope with a difficult parent?"]
    },
    {
      keywords: ['school', 'college', 'university', 'student', 'studying', 'exam', 'exams', 'grades', 'homework', 'academic', 'professor', 'teacher'],
      responses: [
        "Academic pressure can be really intense, and it's okay to feel overwhelmed by it. Your grades don't define your worth as a person. What's been the biggest academic stressor for you lately?",
        "Being a student comes with unique pressures — deadlines, exams, social dynamics, and figuring out your future all at once. That's a lot! Remember to take breaks and be kind to yourself. What's weighing on you the most?",
        "School stress is very real and very valid. Whether it's exam anxiety, workload, or social pressure, you deserve support. One helpful technique is breaking study sessions into 25-minute focused blocks with 5-minute breaks (the Pomodoro Technique). What's going on with school?"
      ],
      followUps: ["I have exam anxiety", "Help me manage my study schedule", "I'm struggling with academic pressure", "I feel like I'm falling behind"]
    },
    {
      keywords: ['eating', 'food', 'weight', 'body image', 'body', 'diet', 'binge', 'appetite', 'not eating', 'overeating'],
      responses: [
        "Our relationship with food and our body can be really complicated. Whether you're struggling with appetite changes, body image, or eating patterns, those feelings are valid and important. Would you like to talk more about what you're experiencing?",
        "Body image and eating concerns affect so many people, and there's no shame in struggling with them. If you're experiencing significant changes in eating habits, it might be helpful to speak with a healthcare provider. In the meantime, I'm here to listen and support you.",
        "Remember that your body is doing its best to take care of you, and it deserves kindness — not criticism. Healing your relationship with food and your body is a journey, not a destination. What's been on your mind around this?"
      ],
      followUps: ["I'm struggling with body image", "My appetite has changed recently", "How can I build a healthier relationship with food?", "When should I seek professional help?"]
    }
  ];

  // track used response indices to avoid repetition
  let usedResponses = {};

  // welcome message when component loads
  onMount(() =>
  {
    const name = firstName ? ` ${firstName}` : '';
    const welcomeMsg =
    {
      role: 'assistant',
      content: `Hi${name}! 👋 I'm your **Wellness Companion** — a safe space to talk about how you're feeling.\n\nI can help with:\n• 💬 Talking through emotions (anxiety, sadness, stress, anger, and more)\n• 🧘 Guided breathing & relaxation exercises\n• 🌟 Affirmations & encouragement\n• 📚 Coping strategies & self-care tips\n• 🆘 Crisis resources when you need them\n\nEverything you share here stays here. How are you feeling today?`,
      timestamp: new Date()
    };
    messages = [welcomeMsg];
    suggestions = ["I'm feeling anxious", "I'm stressed out", "I just need to talk", "What can you help with?"];
  });

  // send message function
  async function sendMessage()
  {
    if (!inputMessage.trim()) return;

    // add user message
    const userMessage =
    {
      role: 'user',
      content: inputMessage,
      timestamp: new Date()
    };

    messages = [...messages, userMessage];
    const currentInput = inputMessage;
    inputMessage = '';
    suggestions = [];
    isTyping = true;
    await scrollToBottom();

    // simulate AI response (** replace with real API call later **)
    await generateResponse(currentInput);
  }

  // use a suggestion chip
  function useSuggestion(text) {
    inputMessage = text;
    sendMessage();
  }

  // generate a response using the response database
  async function generateResponse(userInput)
  {
    // simulate typing delay (vary it slightly for realism)
    const delay = 1200 + Math.random() * 800;
    await new Promise(resolve => setTimeout(resolve, delay));

    let responseText = '';
    let followUps = [];
    const lowerInput = userInput.toLowerCase();

    // find matching category
    let matched = false;
    for (const category of responseDatabase) {
      const isMatch = category.keywords.some(keyword => lowerInput.includes(keyword));
      if (isMatch) {
        // pick a response we haven't used yet for this category
        const key = category.keywords[0];
        if (!usedResponses[key]) usedResponses[key] = [];

        // find unused response
        const available = category.responses
          .map((r, i) => ({ text: typeof r === 'string' ? r : r, index: i }))
          .filter(r => !usedResponses[key].includes(r.index));

        if (available.length === 0) {
          // reset if all used
          usedResponses[key] = [];
          responseText = pick(category.responses);
        } else {
          const chosen = pick(available);
          responseText = chosen.text;
          usedResponses[key].push(chosen.index);
        }

        followUps = category.followUps || [];
        matched = true;
        break;
      }
    }

    // default response if no keywords match
    if (!matched) {
      const defaultResponses = [
        "Thank you for sharing that with me. I'm here to listen without judgment. Can you tell me more about what you're experiencing? The more I understand, the better I can support you.",
        "I appreciate you opening up. Sometimes just putting feelings into words can help. What's the strongest emotion you're feeling right now?",
        "I hear you, and what you're going through matters. Would you like to explore this further, or would you prefer to try a coping exercise like breathing or affirmations?",
        "Thank you for trusting me with that. Let's take this one step at a time. What feels most important for you to address right now?",
        "I'm here for you. Sometimes it helps to talk things through, and other times we need practical tools. What would feel most helpful right now — talking, or trying a calming exercise?"
      ];
      responseText = pick(defaultResponses);
      followUps = ["I'm feeling anxious", "I'm dealing with stress", "Can you share an affirmation?", "Guide me through a breathing exercise"];
    }

    const aiMessage =
    {
      role: 'assistant',
      content: responseText,
      timestamp: new Date()
    };

    messages = [...messages, aiMessage];
    suggestions = followUps;
    isTyping = false;
    await scrollToBottom();
  }

  function handleKeyPress(event)
  {
    if (event.key === 'Enter' && !event.shiftKey)
    {
      event.preventDefault();
      sendMessage();
    }
  }

  function goBack()
  {
    dispatch('back');
  }
</script>

<div class="chatbot-page">
  <div class="chatbot-container">

    <!-- header with back button -->
    <div class="chatbot-header">
      <button class="back-btn" on:click={goBack}>
        ← Back to Resources
      </button>
      <div class="header-content">
          <h2>Wellness Companion</h2>
      </div>
    </div>

    <!-- messages area -->
    <div class="messages-container" bind:this={messagesContainer}>
      {#each messages as message}
        <div class="message {message.role}">
          {#if message.role === 'assistant'}
            <div class="assistant-row">
              <img src="/ava-icon.png" alt="Wellness Companion" class="ava-icon" />
              <div>
                <div class="message-content">
                  {@html message.content
                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                    .replace(/\*(.*?)\*/g, '<em>$1</em>')
                    .replace(/\n/g, '<br>')}
                </div>
                <div class="message-time">
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </div>
              </div>
            </div>
          {:else}
            <div class="message-content">
              {@html message.content
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>')
                .replace(/\n/g, '<br>')}
            </div>
            <div class="message-time">
              {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </div>
          {/if}
        </div>
      {/each}

      {#if isTyping}
        <div class="message assistant">
          <div class="assistant-row">
            <img src="/ava-icon.png" alt="Wellness Companion" class="ava-icon" />
            <div class="message-content typing">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      {/if}
    </div>

    <!-- Suggestion chips -->
    {#if suggestions.length > 0 && !isTyping}
      <div class="suggestions-container">
        {#each suggestions as suggestion}
          <button class="suggestion-chip" on:click={() => useSuggestion(suggestion)}>
            {suggestion}
          </button>
        {/each}
      </div>
    {/if}

    <!-- Input area -->
    <div class="input-container">
      <textarea
        bind:value={inputMessage}
        on:keypress={handleKeyPress}
        placeholder="Share what's on your mind..."
        rows="1"
      ></textarea>
      <button on:click={sendMessage} disabled={!inputMessage.trim()}>
        <span class="send-icon">➤</span>
      </button>
    </div>

    <!-- AI disclaimer -->
    <div class="disclaimer">
      <p>💡 This is an AI assistant, not a replacement for professional mental health care. In crisis, please call 988.</p>
    </div>
  </div>
</div>

<style>
  .chatbot-page
  {
    height: 100vh;
    width: 100%;
    padding: 1.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    background: transparent;
    overflow: hidden;
  }

  .chatbot-container
  {
    display: flex;
    flex-direction: column;
    height: 100%;
    max-width: 750px;
    width: 100%;
    background: #FFFFFF;
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(107, 59, 27, 0.1);
    overflow: hidden;
    border: 1px solid rgba(107, 59, 27, 0.08);
  }

  .chatbot-header
  {
    background: url('/chat-header-bg.png') center bottom / cover no-repeat;
    color: #FFFFFF;
    padding: 1.5rem 1rem;
    position: relative;
  }

  .back-btn
  {
    background: rgba(255, 255, 255, 0.35);
    color: #4a5c48;
    border: none;
    padding: 0.3rem 0.7rem;
    border-radius: 6px;
    cursor: pointer;
    margin-bottom: 0.5rem;
    font-size: 0.8rem;
    font-weight: 600;
    transition: background 0.3s ease;
    text-shadow: none;
  }

  .back-btn:hover
  {
    background: rgba(255, 255, 255, 0.55);
  }

  .header-content
  {
    display: flex;
    align-items: center;
  }

  .chatbot-header h2
  {
    margin: 0;
    font-size: 1.05rem;
    font-weight: 600;
    color: #3d5239;
    text-shadow: 0 1px 2px rgba(255, 255, 255, 0.4);
  }

  .messages-container
  {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    background: #FDF9F7;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .message
  {
    display: flex;
    flex-direction: column;
    max-width: 85%;
    animation: slide-in 0.3s ease-out;
  }

  @keyframes slide-in
  {
    from
    {
      opacity: 0;
      transform: translateY(10px);
    }
    to
    {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .message.user
  {
    align-self: flex-end;
  }

  .message.assistant
  {
    align-self: flex-start;
  }

  .assistant-row
  {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .ava-icon
  {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;
    margin-top: 2px;
    box-shadow: 0 2px 6px rgba(107, 59, 27, 0.12);
  }

  .message-content
  {
    padding: 0.7rem 1rem;
    border-radius: 14px;
    line-height: 1.5;
    font-size: 0.9rem;
  }

  .message.user .message-content
  {
    background: #6B3B1B;
    color: #FFFFFF;
    border-bottom-right-radius: 4px;
  }

  .message.assistant .message-content
  {
    background: #FFFFFF;
    color: #4A4A4A;
    border: 1px solid rgba(107, 59, 27, 0.1);
    border-bottom-left-radius: 4px;
  }

  .message-time
  {
    font-size: 0.75rem;
    color: #4A4A4A;
    margin-top: 0.25rem;
    padding: 0 0.5rem;
    opacity: 0.8;
  }

  .message.user .message-time
  {
    text-align: right;
  }

  .typing
  {
    display: flex;
    gap: 0.5rem;
    padding: 1rem 1.5rem;
  }

  .typing span
  {
    width: 8px;
    height: 8px;
    background: #D57E59;
    border-radius: 50%;
    animation: typing-animation 1.4s infinite;
  }

  .typing span:nth-child(2)
  {
    animation-delay: 0.2s;
  }

  .typing span:nth-child(3)
  {
    animation-delay: 0.4s;
  }

  @keyframes typing-animation
  {
    0%, 60%, 100%
    {
      transform: translateY(0);
    }
    30%
    {
      transform: translateY(-10px);
    }
  }

  .suggestions-container
  {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    padding: 0.5rem 1rem;
    background: #FDF9F7;
    border-top: 1px solid rgba(107, 59, 27, 0.06);
  }

  .suggestion-chip
  {
    background: #FFFFFF;
    color: #6B3B1B;
    border: 1.5px solid rgba(107, 59, 27, 0.2);
    border-radius: 16px;
    padding: 0.35rem 0.75rem;
    font-size: 0.78rem;
    font-family: inherit;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
  }

  .suggestion-chip:hover
  {
    background: #6B3B1B;
    color: #FFFFFF;
    border-color: #6B3B1B;
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(107, 59, 27, 0.2);
  }

  .input-container
  {
    display: flex;
    gap: 0.6rem;
    padding: 0.75rem 1rem;
    background: #FFFFFF;
    border-top: 1px solid rgba(107, 59, 27, 0.08);
  }

  textarea
  {
    flex: 1;
    padding: 0.6rem 0.75rem;
    border: 2px solid rgba(107, 59, 27, 0.12);
    border-radius: 10px;
    font-size: 0.875rem;
    font-family: inherit;
    resize: none;
    max-height: 100px;
    transition: border-color 0.3s ease;
  }

  textarea:focus
  {
    outline: none;
    border-color: #6B9767;
  }

  button
  {
    background: #EBEBEB;
    color: #000000;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 1rem;
    font-weight: 600;
  }

  button:hover:not(:disabled)
  {
    background: #E0E0E0;
    transform: scale(1.02);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }

  button:disabled
  {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .send-icon
  {
    display: inline-block;
  }

  .disclaimer
  {
    background: rgba(250, 226, 188, 0.4);
    padding: 0.5rem 0.75rem;
    text-align: center;
    border-top: 1px solid rgba(107, 59, 27, 0.08);
  }

  .disclaimer p
  {
    margin: 0;
    font-size: 0.75rem;
    color: #6B3B1B;
    font-style: italic;
  }

  @media (max-width: 600px)
  {
    .chatbot-page
    {
      padding: 0.5rem;
    }

    .chatbot-container
    {
      max-width: 100%;
      border-radius: 12px;
    }

    .message
    {
      max-width: 90%;
    }
  }
</style>