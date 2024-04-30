class Priority:
    def __init__(self) -> None:
        self = None
    
    def push(self, data, priority):
        final_queue = []
        final_queue = [(data[i],priority[i]) for i in range(0,len(data))] # item list and priority list to be combined into final_list
        return final_queue 