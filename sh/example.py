from sh import ls, sed, awk, df, grep, wc

def get_file_names(path='.'):
    '''
     return only file names on the current directory
     with bash it looks like
     ls -l | sed -E  -e '1d; s/^([^ ]+ +){8}//'
     will check how piping looks like
    '''
    return sed(ls(path, "-l"), "-E", "-e", '1d; s/^([^ ]+ +){8}//' )

def disk_space_monitoring(perc):
    output = awk(grep(df('-Ph'), "-vE",  "'^Filesystem|tmpfs'"), '{ print $5,$1 }')
    for data in output:
        splitter = data.split('%')[0]
        try:
            perc_data = int(splitter)
            if perc_data > perc:
                print(data)
        except:
            continue