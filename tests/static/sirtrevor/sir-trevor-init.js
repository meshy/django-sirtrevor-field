document.addEventListener('DOMContentLoaded', function() {
  SirTrevor.setDefaults({
    // TODO: Make this use django's staticfiles storage somehow.
    iconUrl: '/static/sirtrevor/sir-trevor-icons.svg'
  });

  var editor = new SirTrevor.Editor({
    el: document.querySelector('.js-st-instance')
  });
});
