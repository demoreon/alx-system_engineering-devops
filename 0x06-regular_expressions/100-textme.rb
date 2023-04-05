#!/usr/bin/env ruby
# Script parses a file.

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
