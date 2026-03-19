<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();
  export let userName = "";

  function goToResources() {
    dispatch('continue');
  }
</script>

<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Quattrocento:wght@400;700&display=swap" rel="stylesheet">
</svelte:head>

<div class="happy-container">
  <div class="happy-card">
    <div class="happy-accent"></div>

    <h1>We're So Happy You're Here!</h1>

    <div class="celebration-icon-wrap">
      <img src="/celebration-icon.png" alt="Celebration" class="celebration-img" />
    </div>

    {#if userName}
      <p class="welcome-message">Welcome, {userName}! ✦</p>
    {/if}

    <p class="subtitle">
      You've taken an important first step in prioritizing your mental health.
      We're here to support you on your journey.
    </p>

    <button class="cta-button" on:click={goToResources}>
      Enter your space →
    </button>
  </div>
</div>

<style>
  .happy-container {
    height: 100vh;
    width: 100%;
    background: linear-gradient(165deg, #FDF9F7 0%, #FAE2BC 40%, #FDF9F7 70%, rgba(107, 151, 103, 0.12) 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    overflow: hidden;
  }

  .happy-card {
    background: #FFFFFF;
    border-radius: 28px;
    padding: 44px 44px 48px;
    max-width: 580px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    box-shadow: 0 8px 40px rgba(107, 59, 27, 0.1), 0 4px 20px rgba(107, 151, 103, 0.12);
    text-align: center;
    animation: fadeInUp 0.6s ease-out;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(107, 151, 103, 0.18);
  }

  .happy-accent {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, #6B9767 0%, #D57E59 100%);
    border-radius: 28px 28px 0 0;
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(24px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  h1 {
    font-family: 'Quattrocento', serif;
    color: #6B3B1B;
    font-size: 2.25rem;
    font-weight: 700;
    margin: 0;
    line-height: 1.25;
    letter-spacing: 0.5px;
  }

  .celebration-icon-wrap {
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: bounce 2.5s ease-in-out 3;
  }

  .celebration-img {
    width: 160px;
    height: 160px;
    object-fit: contain;
  }

  @keyframes bounce {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-4px);
    }
  }

  .welcome-message {
    color: #6B3B1B;
    font-size: 1.35rem;
    font-weight: 600;
    margin: 0;
  }

  .subtitle {
    color: #2a2a2a;
    font-size: 1.05rem;
    line-height: 1.6;
    margin: 0;
    max-width: 440px;
  }

  .cta-button {
    background: linear-gradient(135deg, #6B9767 0%, #5A7C57 100%);
    color: #FFFFFF;
    border: none;
    padding: 16px 44px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(107, 151, 103, 0.35);
  }

  .cta-button:hover {
    background: linear-gradient(135deg, #79A775 0%, #6B9767 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 28px rgba(107, 151, 103, 0.4);
  }

  .cta-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 16px rgba(107, 151, 103, 0.3);
  }

  @media (max-width: 768px) {
    .happy-container {
      padding: 1.5rem;
      padding-right: 8%;
    }

    .happy-card {
      padding: 40px 28px;
      border-radius: 20px;
    }

    h1 {
      font-size: 2rem;
    }

    .welcome-message {
      font-size: 1.2rem;
    }

    .subtitle {
      font-size: 1rem;
    }

    .celebration-img {
      width: 180px;
      height: 180px;
    }
  }

  @media (max-width: 480px) {
    .happy-card {
      padding: 32px 24px;
    }

    h1 {
      font-size: 1.75rem;
    }

    .cta-button {
      padding: 14px 36px;
      font-size: 1rem;
    }
  }
</style>
