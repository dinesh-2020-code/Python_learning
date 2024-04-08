"""
Serialization:
    In computing, serialization (or serialisation) is the process of translating a data structure or object state into a
    format that can be stored (e.g. files in secondary storage devices, data buffers in primary storage devices) or
    transmitted (e.g. data streams over computer networks) and reconstructed later (possibly in a different computer
    environment)

    The whole point of serialising something is so that you can either store it somehow, or send it somewhere else.
    For ex: we've seen that we can't write numbers to a text file.
    Instead, we had to write the individual chars - the digits - that made up the number.
    We took a numerical value, and serialized it into its individual digits

Serialization Standards:
    If serialized data is going to be useful to different programs and computer systems, then it needs to follow a
    well-defined standard. JSON is one such standard.

    The International Standards Organisation (ISO) released the standard `ISO/IEC 21778:2017` in 2017. That standard is
    consistent with the ECMA-404 standard for JSON.

    That means any valid JSON that you create can be read by any standards-compliant JSON parser, anywhere in the world.

    JSON:
        JSON is an open standard (no patent issues) format for saving and interchanging data. JSON is human-readable,
        as numbers, and other objects, are serialized to plain text.
        Applications can include JSON parser, that takes the JSON text, and parses it into a format that the application
        can use. Python includes a `json` module

"""