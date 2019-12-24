class CodeFormatter
  def run
    format_terraform_code
    format_ruby_code
    commit_changes "Commit changes made by code formatters"
  end

  private

  def format_terraform_code
    terraform_directories_in_pr.each do |dir|
      execute "terraform fmt #{dir}"
    end
  end

  def format_ruby_code
    ruby_files_in_pr.each do |file|
      execute "standardrb --fix #{file}" if FileTest.exists?(file)
    end
  end

  def terraform_directories_in_pr
    terraform_files_in_pr
      .map { |f| File.dirname(f) }
      .sort
      .uniq
  end

  def ruby_files_in_pr
    files_in_pr.grep(/\.rb$/)
  end

  def terraform_files_in_pr
    files_in_pr.grep(/\.tf$/)
  end
end
