# frozen_string_literal: true

source 'https://rubygems.org'

# Gems at the top are used to build the site.

gem 'csv'
gem 'faraday-retry', '~> 2.2'
gem 'github-pages', group: :jekyll_plugins
gem 'jekyll', '~> 3.9'
gem 'kramdown-parser-gfm'
source 'https://rubygems.org'
# frozen_string_literal: true
gem 'tzinfo-data'

group :jekyll_plugins do
  gem 'jekyll-github-metadata', '~> 2.16'
  gem 'jekyll-jupyter-notebook'
  gem 'jekyll-redirect-from'
  gem 'jekyll-sitemap'
  gem 'jemoji'
  gem 'just-the-docs'
end

# These tools are use for running tests.
group :development, :test do
  gem 'axe-core-capybara'
  gem 'axe-core-rspec'
  gem 'capybara'
  gem 'capybara-screenshot'
  gem 'rack'
  gem 'rackup'
  gem 'rspec'
  gem 'selenium-webdriver'
  gem 'webrick'
end

group :development, :rubocop do
  gem 'rubocop', require: false
  gem 'rubocop-capybara', require: false
  gem 'rubocop-rspec', require: false
end
