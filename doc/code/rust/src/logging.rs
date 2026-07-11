pub fn example() {
    // lief-doc: example-start
    // Set global level to ERROR
    lief::logging::set_level(lief::logging::Level::ERR);

    {
        // Temporarily set global level to DEBUG (RAII)
        let _scoped = lief::logging::Scoped::new(lief::logging::Level::DEBUG);
        lief::logging::log(lief::logging::Level::DEBUG, "This is a debug message");
    }
    // lief-doc: example-end
}
