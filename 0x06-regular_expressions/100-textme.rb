#!/usr/bin/env ruby
# Textme
puts ARGV[0]
       .scan(/^((\[[+]?[a-zA-Z0-9]+)\]\,|(\[[+]?[a-zA-Z0-9])+\]\,|(\[.*\]))$/)
       .join()
