<script>
  // =============
  // BRAIN SECTION
  // =============

  export let title = "Resource Title";
  export let description = "Description";
  export let link = "#";
  export let icon = "📚";
  export let action = null;  // **can be a function to run (for chatbot)**

  function handleClick(event)
  {
    if (action)
    {
      // If there's an action function, run it instead of following the link
      event.preventDefault();
      action();
    }
  }
</script>

<!-- =============-->
<!-- BODY SECTION -->
<!-- =============-->

<div class="resource-card">
  <a
    href={link}
    target={link.startsWith('http') ? '_blank' : '_self'}
    rel={link.startsWith('http') ? 'noopener noreferrer' : ''}
    on:click={handleClick}
    class="card-link"
  >
    <div class="icon">{icon}</div>
    <h3>{title}</h3>
    <p>{description}</p>
    <span class="arrow">→</span>
  </a>
</div>

<style>
  /* ========*/
  /* STYLING */
  /* ========*/

  .resource-card
  {
  }

  .card-link
  {
    display: block;
    background: #FFFFFF;
    border-radius: 12px;
    padding: 1.25rem 1.1rem 2rem;
    box-sizing: border-box;
    text-decoration: none;
    color: inherit;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(107, 59, 27, 0.08);
    border: 1px solid rgba(107, 59, 27, 0.08);
    position: relative;
    overflow: hidden;
  }

  .card-link::before
  {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(107, 151, 103, 0.04) 0%, rgba(213, 126, 89, 0.04) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .card-link:hover::before
  {
    opacity: 1;
  }

  .card-link:hover
  {
    transform: translateY(-6px);
    box-shadow: 0 8px 28px rgba(107, 59, 27, 0.12);
    border-color: #6B9767;
  }

  .icon
  {
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
    position: relative;
    z-index: 1;
  }

  h3
  {
    font-size: 0.95rem;
    color: #6B3B1B;
    margin-bottom: 0.35rem;
    font-weight: 600;
    position: relative;
    z-index: 1;
  }

  p
  {
    color: #4A4A4A;
    line-height: 1.4;
    margin-bottom: 0.25rem;
    position: relative;
    z-index: 1;
    font-size: 0.8rem;
  }

  .arrow
  {
    color: #D57E59;
    font-size: 1rem;
    font-weight: bold;
    position: absolute;
    bottom: 0.6rem;
    right: 0.75rem;
    transition: transform 0.3s ease;
  }

  .card-link:hover .arrow
  {
    transform: translateX(5px);
  }

  /* responsive design */
  @media (max-width: 768px)
  {
    .card-link
    {
      padding: 0.85rem 1rem;
    }

    h3
    {
      font-size: 1rem;
    }

    .icon
    {
      font-size: 1.75rem;
      margin-bottom: 0.25rem;
    }

    p
    {
      font-size: 0.8rem;
    }
  }
</style>