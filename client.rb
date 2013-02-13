# chef-client configuration
#
# More details can be found at http://docs.opscode.com/config_rb_client.html
#

# The user and group that owns a process. This is required when
# starting any executable as a daemon.
user "root"
group "root"

# The sub-directory for cookbooks on the chef-client. This value
# can be a string or an array of file system locations, processed
# in the specified order. The last cookbook is considered to
# override local modifications.
cookbook_path [
  "/var/lib/chef/cookbooks",
  "/var/lib/chef/site-cookbooks"
]

# The location in which backup files are stored. If this value is empty,
# backup files will be stored in the directory of the target file.
file_backup_path "/var/lib/chef/backup"

# The location in which cookbooks (and other transient data) files
# are stored when they are synchronized with Chef. (This value can also
# be used in recipes to download files with the remote_file resource.)
file_cache_path "/var/lib/chef/cache"

# The location in which to look for node-specific recipes.
node_path "/var/lib/chef/node"

# The location in which a process identification number (pid) is saved.
# An executable, when started as a daemon, will write the pid to the
# specified file.
pid_file "/run/chef/chef-client.pid"

# The location in which log file output files will be saved. If this
# location is set to something other than STDOUT, standard output
# logging will still be performed (otherwise there would be no output
# other than to a file).
log_location "/var/log/chef/client.log"

