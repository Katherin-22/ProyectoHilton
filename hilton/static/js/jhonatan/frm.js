  document.getElementById("select-all").addEventListener("change", function () {
    const checkboxes = document.querySelectorAll(".hotel-checkbox");
    checkboxes.forEach(cb => cb.checked = this.checked);
  });