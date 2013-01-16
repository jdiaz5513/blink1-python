= blink(1)-python

== Ooh, what do I get?

  - __blink1-loadavg.py__: A load average visualizer - fun to watch it slowly glow red as a runaway task starts to kick in
  - More to come...

== How do I use it?

  - For now, blink1-loadavg will only work on Linux. Make sure you have blink1-tool in your path (and in my case, setuid root)
  	- Be sure to change the __NUM_CORES__ value to match the number of CPU cores in your system for extra awesomeness.

== In the works

  - A full python library for Linux/OSX/Win that will support (at minimum) all the features of blink1-tool
