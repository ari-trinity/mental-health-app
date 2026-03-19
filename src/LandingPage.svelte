<script>
  // ==============
  // BRAIN SECTION
  // ===============

  import { createEventDispatcher } from 'svelte';

  // lets us tell the parent "user clicked begin"
  const dispatch = createEventDispatcher();

  // runs when user clicks button
  function handleBegin()
  {
    dispatch('begin');
  }
</script>

<!-- Add Google Font -->
<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Quattrocento:wght@400;700&display=swap" rel="stylesheet">
</svelte:head>

<!-- ============= -->
<!-- BODY SECTION  -->
<!-- ============= -->

<div class="landing-page">

  <!-- flowing animated background -->
  <div class="flowing-background">
    <div class="flow-shape flow-1"></div>
    <div class="flow-shape flow-2"></div>
    <div class="flow-shape flow-3"></div>
    <div class="flow-shape flow-4"></div>
  </div>

  <!-- content in the center -->
  <div class="content">

    <!-- gentle fade-in animation for everything -->
    <div class="fade-in-content">

      <!-- Hero Image with overlaid title -->
      <div class="hero-image-container">
        <div class="overlay-title-left">
          <h1 class="brand-name">BUILD A BETTER</h1>
        </div>
        <div class="overlay-title-right">
          <img src="icon.png" alt="Build a Better You Logo" class="logo-overlay" />
          <h1 class="brand-name-bottom">YOU</h1>
        </div>
        <img src="icon-landing-page.png" alt="Two friendly people waving hello in a peaceful garden setting" class="hero-image" />
      </div>

      <!-- subtitle - intriguing message -->
      <p class="subtitle">
        A community space designed to support your mental health, 
        provide resources, and remind you that you're never alone.
      </p>

      <!-- call-to-action button -->
      <button class="begin-button" on:click={handleBegin}>
        <span class="button-text">Get Started</span>
        <span class="button-icon">→</span>
      </button>

    </div>
  </div>
</div>

<style>
  /* ==================== */
  /* LANDING PAGE STYLING */
  /* =====================*/

  .landing-page
  {
    height: 100vh;
    width: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
  }

  /* ====================*/
  /* FLOWING BACKGROUND  */
  /* ====================*/

  .flowing-background
  {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background:
      radial-gradient(ellipse at center 40%, rgba(253, 245, 230, 0.45) 0%, rgba(253, 245, 230, 0) 55%),
      radial-gradient(ellipse at 30% 50%, rgba(210, 165, 140, 0.15) 0%, transparent 50%),
      radial-gradient(ellipse at 70% 50%, rgba(210, 165, 140, 0.15) 0%, transparent 50%),
      linear-gradient(160deg, #7A9E76 0%, #8BAE88 30%, #92B48E 50%, #8BAE88 70%, #6B9767 100%);
    z-index: 0;
  }

  /* flowing shapes – greens, creams & soft corals to match the photo */
  .flow-shape
  {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.3;
  }

  .flow-1
  {
    width: 500px;
    height: 500px;
    background: linear-gradient(135deg, #6B9767 0%, #79A775 100%);
    top: -100px;
    left: -100px;
    animation: float-1 20s ease-in-out infinite;
  }

  .flow-2
  {
    width: 400px;
    height: 400px;
    background: linear-gradient(135deg, #D2A58C 0%, #E8C4A8 100%);
    bottom: -50px;
    right: -50px;
    opacity: 0.15;
    animation: float-2 18s ease-in-out infinite;
  }

  .flow-3
  {
    width: 400px;
    height: 400px;
    background: linear-gradient(135deg, #FDF5E6 0%, #F5E6D0 100%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.25;
    animation: float-3 22s ease-in-out infinite;
  }

  .flow-4
  {
    width: 300px;
    height: 300px;
    background: linear-gradient(135deg, #79A775 0%, #8BAE88 100%);
    top: 20%;
    right: 20%;
    animation: float-4 16s ease-in-out infinite;
  }

  /* floating animations - each shape moves differently */
  @keyframes float-1
  {
    0%, 100%
    {
      transform: translate(0, 0);
    }
    33% {
      transform: translate(30px, -40px);
    }
    66%
    {
      transform: translate(-20px, 30px);
    }
  }

  @keyframes float-2
  {
    0%, 100%
    {
      transform: translate(0, 0);
    }
    50%
    {
      transform: translate(-40px, -30px);
    }
  }

  @keyframes float-3
  {
    0%, 100%
    {
      transform: translate(-50%, -50%) scale(1);
    }
    50%
    {
      transform: translate(-50%, -50%) scale(1.1);
    }
  }

  @keyframes float-4
  {
    0%, 100%
    {
      transform: translate(0, 0) rotate(0deg);
    }
    50%
    {
      transform: translate(20px, 20px) rotate(5deg);
    }
  }

  /* ================*/
  /* CONTENT STYLING */
  /* =============== */

  .content
  {
    position: relative;
    z-index: 1;
    max-width: 700px;
    width: 100%;
    padding: 10px 20px;
    text-align: center;
    margin: 0 auto;
    max-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .fade-in-content
  {
    animation: fadeInUp 1.2s ease-out;
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 28px;
    padding: 24px 28px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  }

  @keyframes fadeInUp
  {
    from
    {
      opacity: 0;
      transform: translateY(30px);
    }
    to
    {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Hero Image Container with Separate Overlays */
  .hero-image-container
  {
    position: relative;
    margin: 0 auto 0.5rem;
    max-width: 400px;
    border-radius: 20px;
    overflow: visible;
  }

  .hero-image
  {
    width: 100%;
    max-height: 45vh;
    object-fit: contain;
    display: block;
    border-radius: 0;
    box-shadow: none;
    transition: transform 0.3s ease;
    -webkit-mask-image: 
      linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 12%, rgba(0,0,0,1) 88%, rgba(0,0,0,0) 100%),
      linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 15%, rgba(0,0,0,1) 75%, rgba(0,0,0,0) 100%);
    mask-image: 
      linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 12%, rgba(0,0,0,1) 88%, rgba(0,0,0,0) 100%),
      linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 15%, rgba(0,0,0,1) 75%, rgba(0,0,0,0) 100%);
    -webkit-mask-composite: destination-in;
    mask-composite: intersect;
  }

  .hero-image-container:hover .hero-image
  {
    transform: translateY(-5px);
  }

  /* Overlay title - left side */
  .overlay-title-left
  {
    position: absolute;
    top: 30px;
    left: 10px;
    z-index: 10;
  }

  .overlay-title-left .brand-name
  {
    font-family: 'Quattrocento', serif;
    font-size: 1.8rem;
    color: #6B3B1B;
    font-weight: 700;
    margin: 0;
    line-height: 1.2;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);
  }

  /* Overlay title - right side */
  .overlay-title-right
  {
    position: absolute;
    top: 21px;
    right: 62px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.15rem;
  }

  .overlay-title-right .brand-name-bottom
  {
    font-family: 'Quattrocento', serif;
    font-size: 1.8rem;
    color: #6B3B1B;
    font-weight: 800;
    margin: 0;
    line-height: 1.2;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);
  }

  .logo-overlay
  {
    width: 58px;
    height: 64px;
    filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.15));
    object-fit: contain;
  }

  /* Subtitle */
  .subtitle
  {
    font-size: 1.1rem;
    color: #000000;
    line-height: 1.5;
    margin-bottom: 20px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  /* begin button – landing CTA style */
  .begin-button
  {
    background: #EBEBEB;
    color: #000000;
    border: none;
    padding: 14px 40px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    position: relative;
    overflow: hidden;
  }

  .begin-button::before
  {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.5s ease;
  }

  .begin-button:hover::before
  {
    left: 100%;
  }

  .begin-button:hover
  {
    background: #E0E0E0;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
  }

  .begin-button:active
  {
    background: #D5D5D5;
    transform: translateY(0);
  }

  /* button icon */
  .button-icon
  {
    display: inline-block;
    transition: transform 0.3s ease;
    font-size: 1.3rem;
  }

  .begin-button:hover .button-icon /* arrow */
  {
    transform: translateX(5px);
  }

  /* =================================== */
  /* RESPONSIVE DESIGN - Mobile friendly */
  /* =================================== */

  @media (max-width: 768px)
  {
    .content
    {
      padding: 10px 12px;
      max-width: 100%;
    }

    .fade-in-content
    {
      padding: 18px 20px;
    }

    .overlay-title-left .brand-name
    {
      font-size: 1.4rem;
      letter-spacing: 1.5px;
    }

    .overlay-title-right .brand-name-bottom
    {
      font-size: 1.4rem;
      letter-spacing: 1.5px;
    }

    .logo-overlay
    {
      width: 40px;
      height: 44px;
    }

    .hero-image-container
    {
      max-width: 350px;
      margin: 0 auto 0.5rem;
    }

    .hero-image
    {
      max-height: 40vh;
    }

    .subtitle
    {
      font-size: 1rem;
      margin-bottom: 15px;
    }

    .begin-button
    {
      padding: 12px 30px;
      font-size: 1rem;
    }
  }

  @media (max-width: 480px)
  {
    .fade-in-content
    {
      padding: 14px 16px;
    }

    .overlay-title-left .brand-name
    {
      font-size: 1.1rem;
      letter-spacing: 1px;
    }

    .overlay-title-right .brand-name-bottom
    {
      font-size: 1.1rem;
      letter-spacing: 1px;
    }

    .logo-overlay
    {
      width: 32px;
      height: 36px;
    }

    .hero-image-container
    {
      max-width: 100%;
      margin: 0 auto 0.5rem;
    }

    .hero-image
    {
      max-height: 35vh;
    }

    .subtitle
    {
      font-size: 0.95rem;
      padding: 0 10px;
      margin-bottom: 12px;
    }

    .begin-button
    {
      padding: 12px 28px;
      font-size: 0.95rem;
    }
  }
</style>