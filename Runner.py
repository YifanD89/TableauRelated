from tableauhyperapi import HyperProcess,Telemetry,TableName,Connection,CreateMode,TableDefinition,\
Inserter,HyperException,NOT_NULLABLE,NULLABLE,SqlType,escape_name,escape_string_literal
import pandas as pd
import numpy as np
import pantab

df = pd.DataFrame(np.random.randint(0,100,size=(10,4)),columns=list('ABCD'))
# print(df)

parameters = {"log_config": ""}

with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU,parameters=parameters) as hyper:
	pantab.frame_to_hyper(df, "hyperfileName.hyper", table=TableName("Extract","tableName"),hyper_process=hyper)
	result = pantab.frames_from_hyper("hyperfileName.hyper",hyper_process=hyper).keys()
	print(result)