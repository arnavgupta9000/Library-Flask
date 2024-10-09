document.querySelectorAll(".book-card").forEach(card => {
    card.addEventListener("click", function()  {
        // find the nearest form parent and submit it
        this.closest("form").submit();
    });
});