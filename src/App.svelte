<script>
  // ==================
  // import components
  // ==================

  import LandingPage from './LandingPage.svelte';
  import Welcome from './Welcome.svelte';
  import HappyPage from './HappyPage.svelte';
  import Header from './Header.svelte';
  import ResourceCard from './ResourceCard.svelte';
  import ChatBox from './ChatBox.svelte';

  // ============================================
  // TRACKING - Ari Notes
  // #1: "landing" = Landing page
  // #2: "welcome" = Welcome form
  // #3: "happy" = Happy celebration
  // #4: "main" = Main resources page
  // #5:"chatbot" = AI Chatbot (IN PROGRESS!!)
  // ============================================

  let currentPage = "landing";

  // store user's name from welcome page
  let userName = "";

  // ===========
  // FUNCTIONS
  // ===========

  // will run when user clicks "Begin Your Journey" on landing page
  function handleLandingComplete()
  {
    currentPage = "welcome";
  }

  // will run when user submits the Welcome form
  function handleWelcomeComplete(event)
  {
    // save user name
    userName = event.detail.userName;

    // move onto next page (happy page)
    currentPage = "happy";
  }

  // runs when user clicks `continue` on the Happy page
  function handleHappyComplete()
  {
    // move to main app
    currentPage = "main";
  }
  //IN-PROGRESS!!
  // will run when user wants to talk to the AI
  function openChatbot()
  {
    currentPage = "chatbot";
  }
  //IN-PROGRESS!!

  // runs when user wants to go back to resources
  function backToResources()
  {
    currentPage = "main";
  }

  function goHome()
  {
    currentPage = "landing";
  }

  function scrollToResource(index)
  {
    const el = document.getElementById('resource-' + index);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  // ===============
  // RESOURCES DATA
  // ===============

  const resources = [
    {
      title: "Self-Care Guide",
      description: "Simple daily practices for better mental health and wellness",
      link: "https://www.stress.org.uk/wp-content/uploads/2021/05/Self-care-Workbook.pdf",
      icon: "💚"
    },
    {
      title: "Affirmations",
      description: "Daily positive reminders to uplift your spirit and boost confidence",
      link: "#affirmations",
      icon: "💭",
      action: null
    },
    {
      title: "Meditation & Mindfulness",
      description: "Guided practices to calm your mind and find inner peace",
      link: "https://www.uclahealth.org/uclamindful/health-and-wellness-meditations",
      icon: "🧘"
    },
    {
      title: "AI Wellness Companion",
      description: "Chat with our compassionate AI support companion anytime",
      link: "#",
      icon: "🤖",
      action: openChatbot
    },
    {
      title: "Community Support",
      description: "Connect with others on similar journeys and share experiences",
      link: "https://crsok.org/community-resources/",
      icon: "🤝",
      action: null
    },
    {
      title: "Crisis Resources",
      description: "24/7 immediate help when you need someone to talk to",
      link: "https://988lifeline.org/",
      icon: "🆘"
    }
  ];
</script>

<!-- ==================== -->
<!-- ANIMATED BACKGROUND  -->
<!-- ==================== -->
<div class="wave-background">
  <div class="wave wave1"></div>
  <div class="wave wave2"></div>
  <div class="wave wave3"></div>
</div>

<!-- =================================== -->
<!-- BODY SECTION -- Landing Page FIRST! -->
<!-- =================================== -->

{#if currentPage === "landing"}
  <!-- PAGE 0: Landing page -->
  <LandingPage on:begin={handleLandingComplete} />

{:else if currentPage === "welcome"}
  <!-- PAGE 1: Welcome form -->
  <Welcome on:continue={handleWelcomeComplete} on:back={goHome} />

{:else if currentPage === "happy"}
  <!-- PAGE 2: Happy celebration page -->
  <HappyPage userName={userName} on:continue={handleHappyComplete} />

{:else if currentPage === "chatbot"}
  <!-- #4: AI Chatbot -->
  <ChatBox userName={userName} on:back={backToResources} />

{:else if currentPage === "main"}
  <!-- PAGE 3: Main app with resources -->
  <main>
    <Header
      resources={resources}
      onGoToResource={scrollToResource}
      on:home={goHome}
    />

    <section class="resources-section">
      <div class="section-header">
        <h2>Your Wellness Toolkit</h2>
        <p class="section-subtitle">Explore resources designed to support your mental health journey</p>
      </div>

      <div class="resources-grid">
        {#each resources as resource, i}
          <div id="resource-{i}" class="resource-card-wrapper">
            <ResourceCard
              title={resource.title}
              description={resource.description}
              link={resource.link}
              icon={resource.icon}
              action={resource.action}
            />
          </div>
        {/each}
      </div>
    </section>

    <div class="support-message">
      <p>~ Remember: Seeking help is a sign of strength, not weakness ~</p>
    </div>
  </main>
{/if}

<style>
  /* ================================= */
  /* ANIMATED GRADIENT WAVE BACKGROUND */
  /* ================================= */

  .wave-background
  {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #FDF9F7;
    z-index: -1;
    overflow: hidden;
  }

  .wave
  {
    position: absolute;
    width: 200%;
    height: 200%;
    opacity: 0.2;
  }

  .wave1
  {
    background: radial-gradient(ellipse at center, #FAE2BC 0%, transparent 70%);
    animation: wave-animation 15s ease-in-out infinite;
    top: -50%;
    left: -50%;
  }

  .wave2
  {
    background: radial-gradient(ellipse at center, #6B9767 0%, transparent 70%);
    animation: wave-animation 20s ease-in-out infinite reverse;
    top: -30%;
    left: -30%;
    animation-delay: -5s;
  }

  .wave3
  {
    background: radial-gradient(ellipse at center, #D57E59 0%, transparent 70%);
    animation: wave-animation 25s ease-in-out infinite;
    top: -40%;
    left: -40%;
    animation-delay: -10s;
  }

  @keyframes wave-animation
  {
    0%, 100% {
      transform: translate(0, 0) scale(1);
    }
    33% {
      transform: translate(10%, 5%) scale(1.1);
    }
    66% {
      transform: translate(-5%, 10%) scale(0.9);
    }
  }

  /* =============*/
  /* MAIN STYLING */
  /* =============*/

  main
  {
    min-height: 100vh;
    width: 100%;
    position: relative;
    z-index: 1;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1rem;
  }

  .resources-section
  {
    padding: 16px;
    width: min(100%, 980px);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
  }

  /* header section */
  .section-header
  {
    text-align: center;
    margin-bottom: 12px;
    flex-shrink: 0;
  }

  .resources-section h2
  {
    color: #6B3B1B;
    font-size: 1.75rem;
    font-weight: 600;
    margin-bottom: 6px;
    line-height: 1.2;
  }

  .section-subtitle
  {
    color: #4A4A4A;
    font-size: 1rem;
    margin-bottom: 0;
    font-weight: 400;
    line-height: 1.4;
  }

  /* resource cards grid */
  .resources-grid
  {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: auto;
    gap: 12px;
    width: 100%;
    margin: 0 auto;
  }

  .resource-card-wrapper
  {
    min-height: 0;
  }

  .support-message
  {
    background: #5A7C57;
    color: #FFFFFF;
    padding: 14px 20px;
    text-align: center;
    flex: 1;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 20px;
  }

  .support-message p
  {
    font-size: 0.95rem;
    margin: 0;
    opacity: 0.95;
  }

  /* responsive */
  @media (max-width: 900px)
  {
    .resources-grid
    {
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }

    .resources-section h2
    {
      font-size: 1.5rem;
    }

    .section-subtitle
    {
      font-size: 0.9rem;
    }
  }

  @media (max-width: 640px)
  {
    .resources-grid
    {
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }
  }

  @media (max-width: 420px)
  {
    .resources-grid
    {
      grid-template-columns: 1fr;
      gap: 8px;
    }

    .resources-section
    {
      padding: 12px 12px 8px;
    }
  }
</style>