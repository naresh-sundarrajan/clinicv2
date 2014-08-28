// Generated by CoffeeScript 1.6.3
(function() {
  jQuery(function() {
    var $, configureMenus, menu, menuTrigger;
    $ = jQuery;
    menuTrigger = $('#menu-trigger');
    menu = $.offCanvasMenu({
      direction: 'right',
      coverage: '70%'
    });
    (configureMenus = function(display) {
      switch (display) {
        case 'block':
          menu.on();
          break;
        case 'none':
          menu.off();
          break;
        default:
          return;
      }
    })(menuTrigger.css('display'));
    menuTrigger.csswatch({
      props: 'display'
    }).on('css-change', function(event, change) {
      return configureMenus(change.display);
    });
    return FastClick.attach(document.body);
  });

}).call(this);
