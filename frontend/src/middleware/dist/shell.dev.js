"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

/**
 * used to fetch response from my created shell
 */
function postCommand(command) {
  var url, data, response, result;
  return regeneratorRuntime.async(function postCommand$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          url = 'https://www.johnmkagunda.me/api/v1/projects/shell';
          data = {
            command: command
          };
          _context.next = 4;
          return regeneratorRuntime.awrap(fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          }));

        case 4:
          response = _context.sent;

          if (response.ok) {
            _context.next = 7;
            break;
          }

          throw new Error("HTTP error! status: ".concat(response.status));

        case 7:
          _context.next = 9;
          return regeneratorRuntime.awrap(response.json());

        case 9:
          result = _context.sent;

          if (result['$'].includes('\r')) {
            result['$'] = result['$'].replace(/\r/g, ' ');
          }

          console.log(result);
          return _context.abrupt("return", result['$']);

        case 13:
        case "end":
          return _context.stop();
      }
    }
  });
}

var _default = postCommand;
exports.default = _default;