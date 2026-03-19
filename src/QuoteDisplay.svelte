<script>
  // ====================
  // QUOTE DISPLAY LOGIC
  // ====================

  // array of quotes
  const quotes = [
    {
      text: "You are stronger than you think.",
      author: "Unknown"
    },
    {
      text: "One day at a time.",
      author: "Anonymous"
    },
    {
      text: "Your mental health is a priority, not a luxury.",
      author: "Unknown"
    },
    {
      text: "It's okay to not be okay.",
      author: "Anonymous"
    },
    {
      text: "Healing is not linear.",
      author: "Unknown"
    }
  ];

  // choose `RANDOM` quote to show first
  // Math.random() = gives a random decimal between 0 and 1
  // Math.floor() = rounds DOWN to whole number
  // quotes.length = how many quotes we have (5)
  // example: Math.floor(Math.random() * 5) gives us 0, 1, 2, 3, or 4
  let currentQuote = quotes[Math.floor(Math.random() * quotes.length)];

  // picks a new quote when called
  function getNewQuote()
  {
    // "pick another random quote"
    currentQuote = quotes[Math.floor(Math.random() * quotes.length)];
  }
</script>

<!-- ============== -->
<!-- screen display -->
<!-- ============== -->

<div class="quote-container">
  <div class="quote-box">
    <!-- display the quote text -->
    <!-- the '{}'' puts JavaScript values into HTML -->
    <p class="quote-text">"{currentQuote.text}"</p>

    <!-- display author -->
    <p class="quote-author">— {currentQuote.author}</p>

    <!-- button that runs getNewQuote when clicked -->
    <!-- on:click = "when user clicks this" -->
    <!-- {getNewQuote} = "run this function" -->
    <button on:click={getNewQuote}>Get New Quote</button>
  </div>
</div>

<style>
  /* ========*/
  /* STYLING */
  /* ========*/

  /* outer wrapper */
  .quote-container
  {
    padding: 0;
    display: flex;
    justify-content: center;
  }

  .quote-box
  {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 25px 20px;
    width: 100%;
    box-shadow: 0 4px 20px rgba(107, 59, 27, 0.08);
    text-align: center;
    border: 1px solid rgba(107, 59, 27, 0.08);
  }

  .quote-text
  {
    font-size: 1.1rem;
    color: #6B3B1B;
    font-style: italic;
    margin-bottom: 12px;
    line-height: 1.5;
  }

  .quote-author
  {
    color: #4A4A4A;
    font-size: 0.9rem;
    margin-bottom: 20px;
  }

  button
  {
    background: #EBEBEB;
    color: #000000;
    border: none;
    padding: 10px 24px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  }

  button:hover
  {
    background: #E0E0E0;
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
  }
</style>