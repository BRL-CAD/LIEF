#include <LIEF/logging.hpp>

void example() {
  // lief-doc: example-start
  // Set global level to ERROR
  LIEF::logging::set_level(LIEF::logging::LEVEL::ERR);

  {
    // Temporarily set global level to DEBUG (RAII)
    LIEF::logging::Scoped _(LIEF::logging::LEVEL::DEBUG);
    LIEF::logging::log(LIEF::logging::LEVEL::DEBUG, "This is a debug message");
  }
  // lief-doc: example-end
}
