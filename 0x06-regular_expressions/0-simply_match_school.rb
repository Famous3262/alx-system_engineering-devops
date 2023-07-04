#!/usr/bin/env ruby
# Get the argument passed to the script
arg = ARGV[0]

# Define the regular expression to match against
regex = /School/

# Use the regular expression to match against the argument
if arg =~ regex
  puts "The argument matches the regular expression!"
else
  puts "The argument does not match the regular expression."
end
