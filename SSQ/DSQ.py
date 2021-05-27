import numpy as np

np.random.seed(0)


class DSQ:

    def __init__(self, Inter_Arrivals, Service_Time, Discipline):
        self.inter_arrivals = Inter_Arrivals.copy()
        self.service_time = Service_Time.copy()
        self.clock = 0.0
        self.server_status1 = 0  # idle initially
        self.server_status2 = 0  # idle initially
        self.next_arrival_time = self.inter_arrivals.pop(0)
        self.next_departure_time1 = float('inf')
        self.next_departure_time2 = float('inf')
        self.num_in_queue = 0
        self.times_of_arrival_in_queue = []  # store arrival times of the customers in the queue
        self.service_times_in_queue = []  # store service time otf the customers in queue
        self.num_of_delay = 0
        self.total_delay = 0
        self.area_under_qt = 0
        self.area_under_bt1 = 0
        self.area_under_bt2 = 0
        self.last_event_time = 0
        self.discipline = Discipline

    def start(self, number_of_customers):  # start the simulation
        while self.num_of_delay < number_of_customers:  # simulation till number_of_customers customer delay
            self.timing()
        print(f'Average Delay : {self.total_delay / number_of_customers:.3f}')
        print(f'Expected Number of Customers in the queue : {self.area_under_qt / self.clock:.3f}')
        print(f'Expected Utilization of the server-1 : {self.area_under_bt1 / self.clock:.3f}')
        print(f'Expected Utilization of the server-2 : {self.area_under_bt2 / self.clock:.3f}')

    def timing(self):  # clock moves forward according to the next event
        self.clock = min(self.next_arrival_time, self.next_departure_time1, self.next_departure_time2)
        if self.clock == self.next_arrival_time:
            self.arrival()
            self.update_register1()
            self.update_register2()
        elif self.clock == self.next_departure_time1:
            self.departure1()
            self.update_register1()
            self.update_register2()
        else:
            self.departure2()
            self.update_register1()
            self.update_register2()
        self.last_event_time = self.clock

        print("Clock: ", self.clock)
        print("Server Status: -> 1 : " + str(self.server_status1))
        print("Server Status: -> 2 : " + str(self.server_status2))
        print("Number of people Queue: ", self.num_in_queue)
        print("Times of arrivals in Queue: " + str(self.times_of_arrival_in_queue))
        print("Service times in Queue: " + str(self.service_times_in_queue))
        print("Number of Delays: " + str(self.num_of_delay))
        print("Total Delay:" + str(self.total_delay))
        print("Area under Q(t): " + str(self.area_under_qt))
        print("Area under B(t) -> 1: " + str(self.area_under_bt1))
        print("Area under B(t)-> 2: " + str(self.area_under_bt2))
        print("Next Arrival Time: " + str(self.next_arrival_time))
        print("Next Departure Time -> 1: " + str(self.next_departure_time1))
        print("Next Departure Time -> 2: " + str(self.next_departure_time2))
        print(" ")

    def arrival(self):  # arrival algorithm implementation
        self.next_arrival_time = self.next_arrival_time + self.inter_arrivals.pop(
            0)  # schedule next customers arrival time
        if self.server_status1 == 0:
            self.num_of_delay += 1
            self.server_status1 = 1
            self.next_departure_time1 = self.clock + self.service_time.pop(0)  # schedule next departure

        elif self.server_status2 == 0:
            self.num_of_delay += 1
            self.server_status2 = 1
            self.next_departure_time2 = self.clock + self.service_time.pop(0)  # schedule next departure
        else:
            self.num_in_queue += 1  # add 1 to the queue
            self.times_of_arrival_in_queue.append(self.clock)  # store arrival times of the customer in the queue
            self.service_times_in_queue.append(self.service_time.pop(0))  # store service time of the customer in queue

    def departure1(self):  # departure algorithm implementation
        if self.num_in_queue == 0:
            self.server_status1 = 0
            self.next_departure_time1 = float('inf')
        else:
            # if queue not empty
            self.num_in_queue -= 1
            self.num_of_delay += 1

            if self.discipline == 'FIFO':
                # fifo

                arrival = self.times_of_arrival_in_queue.pop(0)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time1 = self.clock + self.service_times_in_queue.pop(0)
            elif self.discipline == 'LIFO':

                # lifo

                arrival = self.times_of_arrival_in_queue.pop(-1)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time1 = self.clock + self.service_times_in_queue.pop(-1)
            else:

                # sjf
                target_index = self.service_times_in_queue.index(min(self.service_times_in_queue))
                arrival = self.times_of_arrival_in_queue.pop(target_index)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time1 = self.clock + self.service_times_in_queue.pop(target_index)

    def departure2(self):  # departure algorithm implementation
        if self.num_in_queue == 0:
            self.server_status2 = 0
            self.next_departure_time2 = float('inf')
        else:
            # if queue not empty
            self.num_in_queue -= 1
            self.num_of_delay += 1

            if self.discipline == 'FIFO':
                # fifo

                arrival = self.times_of_arrival_in_queue.pop(0)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time2 = self.clock + self.service_times_in_queue.pop(0)
            elif self.discipline == 'LIFO':

                # lifo

                arrival = self.times_of_arrival_in_queue.pop(-1)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time2 = self.clock + self.service_times_in_queue.pop(-1)
            else:

                # sjf
                target_index = self.service_times_in_queue.index(min(self.service_times_in_queue))
                arrival = self.times_of_arrival_in_queue.pop(target_index)
                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_time2 = self.clock + self.service_times_in_queue.pop(target_index)

    def update_register1(self):
        time_difference = self.clock - self.last_event_time
        self.area_under_qt = self.area_under_qt + time_difference * self.num_in_queue
        self.area_under_bt1 = self.area_under_bt1 + time_difference * self.server_status1
        # self.last_event_time = self.clock
        # print(time_difference)

    def update_register2(self):

        time_difference = self.clock - self.last_event_time
        self.area_under_qt = self.area_under_qt + time_difference * self.num_in_queue
        self.area_under_bt2 = self.area_under_bt2 + time_difference * self.server_status2


# Inter_Arrivals = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0.7]
# Service_Time = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 1.2, 2.1, 0.5, 1.0]


discipline = ['FIFO', 'LIFO', 'SJF']
customers = [10, 30, 60]

for n in customers:
    for item in discipline:
        inter_arrivals = list(np.random.exponential(1.2, n * 2))
        service_time = list(np.random.exponential(1.3, n * 2))
        s = DSQ(inter_arrivals, service_time, item)
        print()
        print(f'For Discipline = {item} and Customers = {n} : ')
        print()
        s.start(n)
