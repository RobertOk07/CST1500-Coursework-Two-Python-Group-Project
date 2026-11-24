#FCFS
# My process will have a list of [Process number(pn),burst time(),arrival time]
#                                         0        ,     1     ,     2 ---- index

def arrival_time(process):
    return process[2]

def fcfs(process_list):
    t = 0
    process_count = len(process_list)         #remembers how many process i have started with.
    total_waiting = 0
    total_turnaround= 0
    process_position = 0                      #After 1 process finishes, I increase the position by 1 to move to the next process. The loop stops when all processes have been handled.” FOR WHY I REMOVED POP.
    order_of_process = []                     # my order of processes
    completed = {}                            #keeps track of all the process, completion time and turn around time.
    process_list.sort(key=arrival_time)       #sorts my data by arrival time
    while process_position < len(process_list):
        if process_list[process_position][2] > t:
            t += 1
            order_of_process.append("Idle, not in use right now :D")
            continue
        else:
            process = process_list[process_position]
            bt = process[1]                    #burst time, we need a value first that why it is here.
            order_of_process.append(process[0])
            t += bt
            pn = process[0]
            ct = t                              #completion time
            tt = ct - process[2]                #turn around time.
            wt = tt - bt                        #waiting time
            completed[pn] = (ct,tt,wt, bt)      #creating an entry in my table  
            total_waiting += wt                 #calculates my total waiting time after a process and keeps adding it to my number.
            total_turnaround += tt
            process_position += 1
            
    print("CPU Algorithm ONE: First Come First Served (FCFS):", order_of_process)
    print()
    
    for pn in completed:
        ct, tt, wt, bt = completed[pn]         #here i am going through my dictionary and checking my numbers.
        #taking my saved results and putting them into my variables.

        print("-"*30)
        print("Process Number:", pn)
        print("Burst time:", bt)
        print("Waiting time:", wt)
        print("Turnaround time:", tt)
        print("Completion time:", ct)
        print("-"*30)
    
    print("Average waiting time:", total_waiting/process_count)
    print("Average turnaround time:", total_turnaround/process_count) #they have to be outside my loop so they only print ones after all my processes.

if __name__ == "__main__":
    process_list= [["1",5,3],["2",8,5],["3",12,4],["4",15,7],["5",6,8],["6",9,6],["7",8,2],["8",11,1],["9",20,10],["10",2,9]]
    fcfs(process_list)