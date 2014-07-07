(function() {
  this.trace_mode = false;

  this.env = {
    production: false
  };

  this._log = function() {
    try {
      return console.log.apply(console, arguments);
    } catch (_error) {}
  };

  this.log = function() {
    try {
      if (!env.production) {
        return _log.apply(console, arguments);
      }
    } catch (_error) {}
  };

  this.trace = function() {
    try {
      if (trace_mode) {
        return _log.apply(console, arguments);
      }
    } catch (_error) {}
  };

}).call(this);
