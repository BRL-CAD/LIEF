//! Android-specific API
pub mod host;
pub mod module;
pub mod process;
pub mod property;

#[doc(inline)]
pub use module::{dlopen, Module};

#[doc(inline)]
pub use host::Host;

#[doc(inline)]
pub use process::Process;

#[doc(inline)]
pub use property::{Properties, Property};
