(function() {
  this.Slider = {
    in_progress: false,
    container: function() {
      return $('.slider ul');
    },
    lis: function() {
      return $('li', this.container());
    },
    slides_count: function() {
      return this.lis().length;
    },
    slide_width: function() {
      return $('.slider li').width();
    },
    shift: function() {
      return this.container().position().left;
    },
    init: function() {
      var _this = this;
      $(".slider .fwd").click(function() {
        var _shift;
        if (!_this.in_progress) {
          _shift = Math.abs(_this.shift() - _this.slide_width());
          if (!(_shift >= _this.slide_width() * _this.slides_count())) {
            _this.in_progress = true;
            _this.container().animate({
              left: "-=" + (_this.slide_width()) + "px"
            }, 600, function() {
              return _this.in_progress = false;
            });
          }
        }
        return false;
      });
      return $(".slider .bck").click(function() {
        if (!_this.in_progress) {
          if (_this.shift() !== 0) {
            _this.in_progress = true;
            _this.container().animate({
              left: "+=" + (_this.slide_width()) + "px"
            }, 600, function() {
              return _this.in_progress = false;
            });
          }
        }
        return false;
      });
    }
  };

  $(function() {
    return Slider.init();
  });

}).call(this);
