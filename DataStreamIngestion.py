class DataStream:
    def __init__(self):
        self.tstamp: int = None
        self.datastring: str = None
        self.result_list : list = []
    def should_output_data_str(self, timestamp:int, data_string:str)->bool:
        if self.datastring!= data_string:
            self.datastring = data_string
            self.tstamp = timestamp
            return True
        elif self.datastring == data_string:
            if self.tstamp + 5 < timestamp:
                self.datastring = data_string
                self.tstamp = timestamp
                return True
        return False
        
DS = DataStream()
data_stream = DataStream()
data_stream.should_output_data_str(timestamp=0, data_string="hello")
data_stream.should_output_data_str(timestamp=1, data_string="world")
data_stream.should_output_data_str(timestamp=6, data_string="hello")
data_stream.should_output_data_str(timestamp=7, data_string="hello")
data_stream.should_output_data_str(timestamp=8, data_string="world")

