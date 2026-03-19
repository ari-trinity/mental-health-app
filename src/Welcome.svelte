<script>
  // ==============
  // BRAIN SECTION
  // ==============

  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let userName = "";
  let userEmail = "";
  let userPassword = "";

  function handleSubmit()
  {
    if (userName && userEmail && userPassword)
    {
      // send the name along with the continue event
      dispatch('continue', { userName: userName });
    }
  }

  function goBack()
  {
    dispatch('back');
  }
</script>

<!-- ============ -->
<!-- BODY SECTION -->
<!-- ============ -->

<div class="welcome-container">
  <div class="welcome-box">
    <div class="welcome-accent"></div>
    <button type="button" class="back-btn" on:click={goBack}>← Back</button>

    <!-- Top group: illustration + title + subtitle -->
    <div class="top-group">
    <div class="illustration-wrapper">
      <svg viewBox="0 0 400 140" xmlns="http://www.w3.org/2000/svg" class="calming-illustration">
        <!-- Large sage green blob - left -->
        <ellipse cx="80" cy="75" rx="70" ry="55" fill="#8BAE88" opacity="0.35">
          <animate attributeName="rx" values="70;75;70" dur="8s" repeatCount="indefinite" />
          <animate attributeName="ry" values="55;50;55" dur="8s" repeatCount="indefinite" />
        </ellipse>

        <!-- Peachy-coral blob - right -->
        <ellipse cx="310" cy="65" rx="65" ry="50" fill="#D57E59" opacity="0.25">
          <animate attributeName="rx" values="65;60;65" dur="7s" repeatCount="indefinite" />
          <animate attributeName="ry" values="50;55;50" dur="7s" repeatCount="indefinite" />
        </ellipse>

        <!-- Small sage circle - top center -->
        <circle cx="200" cy="30" r="25" fill="#6B9767" opacity="0.2">
          <animate attributeName="cy" values="30;35;30" dur="6s" repeatCount="indefinite" />
        </circle>

        <!-- Soft coral circle - center left -->
        <circle cx="150" cy="90" r="18" fill="#E8A889" opacity="0.3">
          <animate attributeName="cx" values="150;155;150" dur="9s" repeatCount="indefinite" />
        </circle>

        <!-- Tiny sage dot -->
        <circle cx="260" cy="110" r="10" fill="#79A775" opacity="0.25">
          <animate attributeName="r" values="10;12;10" dur="5s" repeatCount="indefinite" />
        </circle>

        <!-- Flowing curve - sage green -->
        <path d="M 0 100 Q 100 60, 200 85 T 400 70" fill="none" stroke="#6B9767" stroke-width="2" opacity="0.2">
          <animate attributeName="d" values="M 0 100 Q 100 60, 200 85 T 400 70;M 0 95 Q 100 70, 200 80 T 400 75;M 0 100 Q 100 60, 200 85 T 400 70" dur="10s" repeatCount="indefinite" />
        </path>

        <!-- Flowing curve - peachy coral -->
        <path d="M 0 60 Q 100 90, 200 55 T 400 80" fill="none" stroke="#D57E59" stroke-width="1.5" opacity="0.18">
          <animate attributeName="d" values="M 0 60 Q 100 90, 200 55 T 400 80;M 0 65 Q 100 85, 200 60 T 400 75;M 0 60 Q 100 90, 200 55 T 400 80" dur="12s" repeatCount="indefinite" />
        </path>

        <!-- Medium peachy blob - center -->
        <ellipse cx="200" cy="70" rx="40" ry="30" fill="#E8C4A8" opacity="0.2">
          <animate attributeName="rx" values="40;45;40" dur="9s" repeatCount="indefinite" />
        </ellipse>
      </svg>
    </div>

    <h1>Welcome to Your Safe Space</h1>
    <p class="subtitle">Let's set things up so we can support you best.</p>
    </div>

    <form on:submit|preventDefault={handleSubmit}>

      <div class="input-group">
        <label for="name">Your Name</label>
        <input
          type="text"
          id="name"
          placeholder="Enter your name"
          bind:value={userName}
          required
        />
      </div>

      <div class="input-group">
        <label for="email">Your Email</label>
        <div class="email-input-wrapper">
          <input
            type="email"
            id="email"
            placeholder="Enter your email"
            bind:value={userEmail}
            required
          />
          <span class="lock-icon">🔒</span>
        </div>
      </div>

      <div class="input-group">
        <label for="password">Your Password</label>
        <div class="email-input-wrapper">
          <input
            type="password"
            id="password"
            placeholder="Create a password"
            bind:value={userPassword}
            required
          />
          <span class="lock-icon">🔒</span>
        </div>
      </div>

      <p class="privacy-note">Your information is encrypted and secure</p>

      <!-- SUBMIT BUTTON! -->
      <button type="submit">Let's Get Started →</button>
    </form>
  </div>
</div>

<style>
  .welcome-container
  {
    height: 100vh;
    width: 100%;
    background: 
      radial-gradient(ellipse at 20% 30%, rgba(107, 151, 103, 0.15) 0%, transparent 50%),
      radial-gradient(ellipse at 80% 70%, rgba(213, 126, 89, 0.12) 0%, transparent 50%),
      linear-gradient(165deg, #FDF9F7 0%, #FAE2BC 35%, #E8C4A8 55%, #FDF9F7 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    overflow: hidden;
  }

  .welcome-box
  {
    background: rgba(255, 255, 255, 0.92);
    border-radius: 20px;
    padding: 1.5rem 2.5rem 3.5rem;
    max-width: 480px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.75rem;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(107, 59, 27, 0.1), 0 2px 12px rgba(107, 151, 103, 0.08);
    text-align: center;
    border: 1px solid rgba(107, 151, 103, 0.25);
    position: relative;
  }

  .welcome-accent
  {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, #6B9767 0%, #8BAE88 40%, #D57E59 70%, #E8A889 100%);
    border-radius: 28px 28px 0 0;
  }

  .back-btn
  {
    position: absolute;
    top: 14px;
    left: 14px;
    z-index: 2;
    background: rgba(107, 59, 27, 0.08);
    border: none;
    color: #6B3B1B;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    padding: 0.3rem 0.7rem;
    border-radius: 6px;
    transition: background 0.3s ease;
  }

  .back-btn:hover
  {
    background: rgba(107, 59, 27, 0.18);
  }

  .back-btn:focus,
  .back-btn:focus-visible
  {
    outline: none;
    box-shadow: none;
  }

  .back-btn:active
  {
    background: rgba(107, 59, 27, 0.25);
  }

  .top-group
  {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.3rem;
  }

  .illustration-wrapper
  {
    width: 100%;
  }

  .calming-illustration
  {
    width: 100%;
    max-height: 130px;
    display: block;
  }

  h1
  {
    color: #6B3B1B;
    font-size: 1.65rem;
    margin: 0;
    line-height: 1.25;
    font-weight: 700;
  }

  .subtitle
  {
    color: #6B3B1B;
    font-size: 0.9rem;
    margin: 0;
    line-height: 1.4;
    opacity: 0.85;
  }

  form
  {
    text-align: left;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .input-group
  {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  label
  {
    display: block;
    color: #6B3B1B;
    font-weight: 600;
    font-size: 0.82rem;
  }

  input
  {
    width: 100%;
    padding: 9px 14px;
    border: 2px solid rgba(107, 151, 103, 0.25);
    border-radius: 10px;
    font-size: 0.88rem;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
    box-sizing: border-box;
    background: #FDF9F7;
  }

  input:focus
  {
    outline: none;
    border-color: #6B9767;
    box-shadow: 0 0 0 4px rgba(107, 151, 103, 0.15);
  }

  input::placeholder
  {
    color: #6B3B1B;
    opacity: 0.5;
  }

  .email-input-wrapper
  {
    position: relative;
  }

  .email-input-wrapper input
  {
    padding-right: 45px;
  }

  .lock-icon
  {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.1rem;
    opacity: 0.5;
  }

  .privacy-note
  {
    color: #5A7C57;
    font-size: 0.76rem;
    margin: 0;
    font-weight: 600;
    font-style: normal;
    opacity: 1;
    background: rgba(107, 151, 103, 0.08);
    padding: 6px 12px;
    border-radius: 8px;
    border-left: 3px solid #6B9767;
    border-right: 3px solid #6B9767;
    text-align: center;
  }

  button
  {
    width: 100%;
    background: linear-gradient(135deg, #6B9767 0%, #5A7C57 100%);
    color: #FFFFFF;
    border: none;
    padding: 11px 24px;
    border-radius: 50px;
    font-size: 0.92rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 0.25rem;
    box-shadow: 0 4px 16px rgba(107, 151, 103, 0.35);
  }

  button:hover
  {
    background: linear-gradient(135deg, #79A775 0%, #6B9767 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(107, 151, 103, 0.4);
  }

  button:active
  {
    transform: translateY(0);
    box-shadow: 0 2px 12px rgba(107, 151, 103, 0.3);
  }

/* ================= */
/* responsive design */
/* ================= */

@media (max-width: 768px)
{
  .welcome-container
  {
    padding: 1.5rem;
  }

  .welcome-box
  {
    padding: 1.5rem 1.75rem;
    padding-top: 2rem;
  }

  h1
  {
    font-size: 1.4rem;
  }

  .subtitle
  {
    font-size: 0.82rem;
  }
}

@media (max-width: 480px)
{
  .welcome-container
  {
    padding: 0.75rem;
  }

  .welcome-box
  {
    max-width: 100%;
    padding: 1.25rem 1.25rem;
    padding-top: 2rem;
    border-radius: 16px;
    gap: 0.7rem;
  }

  h1
  {
    font-size: 1.3rem;
  }

  .subtitle
  {
    font-size: 0.78rem;
  }

  button
  {
    font-size: 0.88rem;
    padding: 10px 20px;
  }
}
</style>