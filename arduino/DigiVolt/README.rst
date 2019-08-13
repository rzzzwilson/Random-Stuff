DigiVolt
========

Arduino code to handle an MCP42100 digital potentiometer while measuring
a voltage between 0 and (say) 50 volts.

The idea is to use the internal 2.56 volt internal reference and use the
digital pot to approximate the divided voltage to the internal reference.
Care must be taken to:

1. Never apply more than 2.56 volts to the measuring pin, and
2. Never exceed the 1mA current out limit of the digital pot wiper.
