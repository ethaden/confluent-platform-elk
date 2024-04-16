import sys
import pandas

from pathlib import Path

# Change the following lines to match your CSV file format
node_name_column='container.labels.com_docker_compose_service'
message_column='message'

def parse_log_files(csv_file: Path):
    df = pandas.read_csv(csv_file)
    node_names = sorted(df[node_name_column].unique())
    print (node_names)
    for node_name in node_names:
        filename = node_name+'.log'
        print ('Creating file '+filename)
        file = Path(filename)
        with open(file, 'w') as f:
            df_node = df.loc[df[node_name_column]==node_name]
            #dfAsString = df_node.to_string(columns=[message_column], header=False, index=False, justify='left')
            #f.write(dfAsString)
            for line in df[message_column].tolist():
                f.write(line+'\n')
                print (line)

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print ('Usage: python3 extract-log-files.py <filename of csv file exported by kibana>')
        exit (1)
    csv_file = Path(sys.argv[1])
    if not csv_file.exists():
        print ('Error: CSV file does not exist')
        exit (1)
    parse_log_files(csv_file)

