Result of Question 01
algo=default 
# Perform a doubling test for default sort with 100 trials
starting with n = 64
n:      64 time: 0.000998 (n:n/2) ratio: -
n:     128 time: 0.001998 (n:n/2) ratio: 2.001911
n:     256 time: 0.006995 (n:n/2) ratio: 3.501313
n:     512 time: 0.016990 (n:n/2) ratio: 2.428786
n:    1024 time: 0.036978 (n:n/2) ratio: 2.176403
n:    2048 time: 0.090949 (n:n/2) ratio: 2.459532
n:    4096 time: 0.191890 (n:n/2) ratio: 2.109873
n:    8192 time: 0.445746 (n:n/2) ratio: 2.322924
n:   16384 time: 0.934463 (n:n/2) ratio: 2.096403
n:   32768 time: 2.267697 (n:n/2) ratio: 2.426738
n:   65536 time: 4.523405 (n:n/2) ratio: 1.994713
n:  131072 time: 10.480979 (n:n/2) ratio: 2.317055



Question 2)
A)
By using the name start with underscore means we can’t able to import the object. Without underscore use only to avoid the conflict with python library.
B)
Because working with tuple is faster and the data in tuple is save. Tuple value can’t be changeable, if we use list then data maybe change that become a problem during sorting.
C)
Time () function get the current time during the run time. It provide the current value of time. In our function it take the current time in variable start_time and the end return the running time of provide merge algorithm by subtract the time to start_time. 
D)
In the mention junk of code, n stand for the number of element and algorithm represent the sorting algorithm e.g. Bubble sort and etc. In the last variable is represent the is_reverse. If the the value of is_reverse is true by getting the even number. Then algorithm arrange the number in reverse order. 
First of all we check for all value the number is even or odd. If number is even then sort the array in reverse order. In the next step we check the algorithm condition. Apply if else condition in this we selected algorithm call the own function for the sorting. 




Question 06
algo=merge


# Perform a doubling test for merge sort with 100 trials
starting with n = 64
n:      64 time: 0.033980 (n:n/2) ratio: -
n:     128 time: 0.088949 (n:n/2) ratio: 2.617708
n:     256 time: 0.178895 (n:n/2) ratio: 2.011204
n:     512 time: 0.384797 (n:n/2) ratio: 2.150962
n:    1024 time: 1.451152 (n:n/2) ratio: 3.771211
n:    2048 time: 1.846940 (n:n/2) ratio: 1.272740
n:    4096 time: 4.217579 (n:n/2) ratio: 2.283550
n:    8192 time: 12.833616 (n:n/2) ratio: 3.042887
n:   16384 time: 25.444395 (n:n/2) ratio: 1.982636
n:   32768 time: 60.453298 (n:n/2) ratio: 2.375898



algo=bubble

# Perform a doubling test for bubble sort with 100 trials
starting with n = 64
n:      64 time: 0.068959 (n:n/2) ratio: -
n:     128 time: 0.271843 (n:n/2) ratio: 3.942065
n:     256 time: 1.248277 (n:n/2) ratio: 4.591910
n:     512 time: 4.995130 (n:n/2) ratio: 4.001619
n:    1024 time: 21.107883 (n:n/2) ratio: 4.225692
n:    2048 time: 80.033060 (n:n/2) ratio: 3.791620
n:    4096 time: 353.687752 (n:n/2) ratio: 4.419271


algo=insertion

# Perform a doubling test for insertion sort with 100 trials
starting with n = 64
n:      64 time: 0.035978 (n:n/2) ratio: -
n:     128 time: 0.140918 (n:n/2) ratio: 3.916833
n:     256 time: 0.584663 (n:n/2) ratio: 4.148954
n:     512 time: 2.389627 (n:n/2) ratio: 4.087185
n:    1024 time: 10.823786 (n:n/2) ratio: 4.529487
n:    2048 time: 46.557597 (n:n/2) ratio: 4.301415
n:    4096 time: 195.303038 (n:n/2) ratio: 4.194869


Hypothesis 


we can see the number of element and required time ratio for all algoritham.Fastest performance become when we use the default. In other three case have a varitaion. As we increase the value of n then over all ration and time consumming become increase. In the case of merge sort is little time required as compare two others.

The overall ration wise algoritham arrange as 
default-->murge--->insertion--->bubble

in the last iteration for n =4096 the bubble sort move to ward infinity loop. In short term can't able to sort these number of sample in short time.
 