search.addEventListener("input", function () {
    let input = search.value.toLowerCase();
    let rows = document.querySelectorAll("table tbody tr");

    rows.forEach(function (row) {
    //   let nom = row.cells[0].textContent.toLowerCase();
      let cells = Array.from(row.cells)
    //   let resultat = nom.includes(input);
      let match = cells.some(cell => cell.textContent.toLowerCase().includes(input))
      
      row.style.display = match ? "" : "none";
    });
});