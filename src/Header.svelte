<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  export let resources = [];
  export let onGoToResource = (_index) => {};

  let menuOpen = false;

  function goHome() {
    menuOpen = false;
    dispatch('home');
  }

  function toggleMenu() {
    menuOpen = !menuOpen;
  }

  function selectResource(index) {
    onGoToResource(index);
    menuOpen = false;
  }

  function handleKeydown(event) {
    if (event.key === 'Escape') menuOpen = false;
  }
</script>

<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
</svelte:head>

<svelte:window on:keydown={handleKeydown} />

<header class="toolkit-header">
  <div class="header-inner">
    <div class="header-center">
      <div class="brand-group" on:click={goHome} role="button" tabindex="0" on:keydown={(e) => e.key === 'Enter' && goHome()}>
        <span class="brand-left">Build a Better</span>
        <img src="/icon.png" alt="Build a Better You" class="home-icon" />
        <span class="brand-right">You</span>
      </div>
      <p class="tagline">Where personal growth feels good</p>
    </div>

    <button
      type="button"
      class="hamburger"
      aria-label="Open menu"
      aria-expanded={menuOpen}
      on:click={toggleMenu}
    >
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
  </div>

  {#if menuOpen}
    <div class="menu-overlay" role="button" tabindex="-1" on:click={toggleMenu} on:keydown={(e) => e.key === 'Enter' && toggleMenu()}></div>
    <nav class="resource-menu" aria-label="Resources">
      <ul>
        {#each resources as resource, i}
          <li>
            <button
              type="button"
              class="menu-item"
              on:click={() => selectResource(i)}
            >
              <span class="menu-icon">{resource.icon}</span>
              <span>{resource.title}</span>
            </button>
          </li>
        {/each}
      </ul>
    </nav>
  {/if}
</header>

<style>
  .toolkit-header {
    background: #5A7C57;
    color: #FFFFFF;
    padding: 14px 20px;
    box-shadow: 0 4px 16px rgba(90, 124, 87, 0.25);
    position: relative;
    flex-shrink: 0;
  }

  .header-inner {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

  .header-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    border: none;
    background: transparent;
    border-radius: 8px;
    padding: 4px 8px;
    transition: background 0.2s ease, transform 0.2s ease;
  }

  .brand-group:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: scale(1.02);
  }

  .brand-group:focus-visible {
    outline: 2px solid #FAE2BC;
    outline-offset: 2px;
  }

  .brand-left,
  .brand-right {
    font-size: 1.8rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }

  .home-icon {
    width: 38px;
    height: 44px;
    object-fit: contain;
    display: block;
  }

  .tagline {
    margin: 0;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    font-weight: 400;
    opacity: 1;
    color: #FAE2BC;
    text-align: center;
    letter-spacing: 1px;
  }

  .hamburger {
    position: absolute;
    left: 0;
    top: 0;
    flex-shrink: 0;
    width: 48px;
    height: 48px;
    padding: 10px;
    background: rgba(255, 255, 255, 0.15);
    border: 2px solid rgba(255, 255, 255, 0.4);
    cursor: pointer;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 7px;
    transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
    z-index: 10;
  }

  .hamburger:hover {
    background: rgba(255, 255, 255, 0.28);
    border-color: rgba(255, 255, 255, 0.6);
    transform: scale(1.05);
  }

  .hamburger:focus-visible {
    outline: 2px solid #FAE2BC;
    outline-offset: 2px;
  }

  .hamburger-line {
    width: 30px;
    height: 3px;
    background: #FFFFFF;
    border-radius: 2px;
    display: block;
  }

  .menu-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.35);
    z-index: 100;
    animation: fadeIn 0.2s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  .resource-menu {
    position: absolute;
    top: 100%;
    left: 0;
    margin-top: 4px;
    background: #FFFFFF;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(107, 59, 27, 0.15);
    min-width: 260px;
    max-width: 320px;
    z-index: 101;
    overflow: hidden;
    animation: slideDown 0.25s ease;
  }

  @keyframes slideDown {
    from {
      opacity: 0;
      transform: translateY(-8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .resource-menu ul {
    list-style: none;
    margin: 0;
    padding: 8px 0;
  }

  .resource-menu li {
    margin: 0;
  }

  .menu-item {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 20px;
    background: none;
    border: none;
    font-size: 1rem;
    color: #6B3B1B;
    text-align: left;
    cursor: pointer;
    transition: background 0.2s ease;
    font-family: inherit;
  }

  .menu-item:hover {
    background: #FDF9F7;
  }

  .menu-icon {
    font-size: 1.35rem;
  }

  @media (max-width: 600px) {
    .brand-left,
    .brand-right {
      font-size: 1.1rem;
    }

    .home-icon {
      width: 36px;
      height: 42px;
    }

    .brand-group {
      gap: 5px;
    }

    .tagline {
      font-size: 0.95rem;
    }
  }
</style>
