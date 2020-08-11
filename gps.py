import math

class Gps_Calculator:
    #Constructor
    def __init__(self, lat = "", long = "", time = ""):
        self.latitude = lat
        self.longitute = long
        self.time = time
        
    #Distance calculator
    def calc_distance_flt(self, lat_start = 0.0, lat_end = 0.0, long_start = 0.0, long_end = 0.0):
        #Convert to radians
        lat_start = math.radians(lat_start)
        lat_end = math.radians(lat_end)
        long_start = math.radians(long_start)
        long_end = math.radians(long_end)
        #Find the difference between start and end points
        lat_diff = lat_end - lat_start
        long_diff = long_end - long_start
        #Perform computations to find the distance
        x = math.pow( math.sin( lat_diff / 2 ), 2)
        y = math.cos( lat_start ) * math.cos( lat_end ) * math.pow( math.sin( long_diff / 2 ),2 )
        a = x + y
        #a = math.sqrt( math.sin( lat_diff / 2 ) ) + math.cos( lat_start ) * math.cos( lat_end ) * math.sqrt( math.sin( long_diff / 2 ) )
        c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
        #return the distance in miles
        return 3961 * c
    
    #Distance calculator with string input and out
    def calc_distance_str(self, lat_start = "", lat_end = "", long_start = "", long_end = ""):
        #Convert to radians
        lat_start = math.radians(float(lat_start))
        lat_end = math.radians(float(lat_end))
        long_start = math.radians(float(long_start))
        long_end = math.radians(float(long_end))
        #Find the difference between start and end points
        lat_diff = lat_end - lat_start
        long_diff = long_end - long_start
        #Perform computations to find the distance
        x = math.pow( math.sin( lat_diff / 2 ), 2)
        y = math.cos( lat_start ) * math.cos( lat_end ) * math.pow( math.sin( long_diff / 2 ),2 )
        a = x + y
        #a = math.sqrt( math.sin( lat_diff / 2 ) ) + math.cos( lat_start ) * math.cos( lat_end ) * math.sqrt( math.sin( long_diff / 2 ) )
        c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
        #return the distance in miles
        return str(3961 * c)
    
    #Calculate the time difference string input
    def calc_time_diff(self, start_time = "", stop_time = ""):
        #Parse out the start time string
        t = start_time.split(":")
        #find the time in seconds
        hour = int(t[0])*3600
        min = int(t[1])*60
        sec = int(t[2])
        #Add up the seconds
        start_total = hour + min + sec
        #Parse out the stop time string
        t = stop_time.split(":")
        hour = int(t[0])*3600
        min = int(t[1])*60
        sec = int(t[2])
        #Add up the second
        stop_total = hour + min + sec
        #return the difference in seconds
        return abs(stop_total - start_total)
	
	#Compute the rate of travel.
    def cal_rate_of_travel(dist_start = 0.0, dist_end = 0.0, time = 0):
        return abs(dist_end - dist_start) / time
        
class Report_Printer:
	#Constructor
    def print_report_gretting(self)
        print("Welcome to Running Mate\n") 
	
	#Default report header
    def print_report_header(self):
        print("----------------------------------------------------------------------")
        print("Time        Longitude        Latitude        Distance        Pace")
        print("(hh:mm:ss)  (deg)            (deg)           (miles)         (min/mile)")
        print("----------------------------------------------------------------------")
	
	#Print data
    def print_data(self, time = "", long = "", lat = "", dist = "", speed = ""):
        print(time, long, lat, dist, speed)
    
	#Return formatted time.
	def convert_to_time(self, timeInSeconds = 0):
        hour = str(int(timeInSeconds / 3600))
        minute = str( int((timeInSeconds / 60) % 60))
        seconds = str( int(timeInSeconds % 60))
        return hour + ":" + minute + ":" + seconds 
    
        
           
def main():
    gpc =  Gps_Calculator("","","")
    rpptr = Report_Printer()
    end_lat = 0.0
    end_long = 0.0
    time = ""

    #todo: get user input for file locaiton
    fileio = open("..\\gps_data.txt", "r")

    rpptr.print_report_header()
    for fileline in fileio:
        #Split up the line
        t = fileline.split()
        if ((end_lat != 0.0) and (end_long != 0.0)):
            #compute the distance
            dist = str(gpc.calc_distance_flt(float(t[1]), end_lat, float(t[2]), end_long))
            #compute the time difference
            time = gpc.calc_time_diff(time, t[0])
            rpptr.print_data(t[0], t[1], t[2], dist, str(time))
        else:
           rpptr.print_data(t[0], t[1], t[2], "****", "****")

        

        time = t[0]
        end_lat = float(t[1])
        end_long = float(t[2])
            
   
        

        #chceck if the distance and pace is empty
        #compute distance
        #compute pace
        #print time, lat, long, distance, and pace
        #go to next line

        #keep track of fastest speed

    fileio.close()
    

   
if __name__ == "__main__":
    main()

        
    
    

