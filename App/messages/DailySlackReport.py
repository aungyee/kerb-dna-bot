import sys
sys.path.append('..')

import pandas as pd
from datasource.KerbSnowflake import querySnowflake


def getMessage():

    data = querySnowflake('SELECT * FROM KERB.STG_KERB.DAILY_SLACK_REPORT;')

    column_raw = querySnowflake(
        """
        SELECT COLUMN_NAME 
        FROM KERB.INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'STG_KERB' 
            AND TABLE_NAME = 'DAILY_SLACK_REPORT' 
        ORDER BY ORDINAL_POSITION;
        """
    )
    column_names = []
    for column in column_raw:
        column_names.append(column[0])

    df = pd.DataFrame(data, columns = column_names)
    df.drop(columns='ATTRIBUTE_ID', inplace=True)
    latestDf = df[df['EVENT_DATE'] == max(df['EVENT_DATE'])]

    message = '*📅 Date: ' + str(max(df['EVENT_DATE'])) + '*\n\n'
    for index, row in latestDf.iterrows():
        for i in range(1, len(row)):
            message += f'*{latestDf.columns[i]}*: _{row[i]}_\n'
        message += '\n\n'

    return message


if __name__ == '__main__':
    getMessage()
