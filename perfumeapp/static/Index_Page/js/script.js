
    const dropdownButtons = document.querySelectorAll(".dropdown-btn");

    dropdownButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const dropdown = btn.nextElementSibling;
        const arrow = btn.querySelector(".arrow");

        // Toggle display
        dropdown.style.display = dropdown.style.display === "flex" ? "none" : "flex";

        // Rotate arrow
        arrow.classList.toggle("rotate");
      });
    });
