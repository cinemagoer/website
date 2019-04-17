document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.navbar-burger').forEach(function(el) {
    el.addEventListener('click', function() {
      el.classList.toggle('is-active');
      document.getElementById(el.dataset.target).classList.toggle('is-active');
    });
  });
});
