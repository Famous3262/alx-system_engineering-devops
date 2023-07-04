#!/usr/bin/env ruby
# Get the argument passed to the script
input = ARGV[0]

# Define the regular expression to match against
regex = Oniguruma::ORegexp.new('School')

# Use the regular expression to match against the argument
if regex.match(input)
  puts "The string '#{input}' matches the regular expression 'School'"
else
  puts "The string '#{input}' does not match the regular expression 'School'"
end
