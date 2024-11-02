def combine_filenames_to_df(filenames):
    # List to hold DataFrames for each file
    dataframes = []
    
    # Read each file and append to the list
    for filename in filenames:
        df = pd.read_csv(filename, sep='\t')
        dataframes.append(df)
    
    # Concatenate all DataFrames in the specified order
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    return combined_df
