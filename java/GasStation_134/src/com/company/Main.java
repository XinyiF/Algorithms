package com.company;
//There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
//You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
// You begin the journey with an empty tank at one of the gas stations.
//Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

public class Main {
    public static int canCompleteCircuit(int[] gas, int[] cost){
        int i=0,rest=0,stop=1,j,star=i,sum_gas=0,sum_cost=0;
        for(int k=0;k<gas.length;k++){
            sum_gas+=gas[k];
            sum_cost+=cost[k];
        }
        if(sum_gas<sum_cost){
            return -1;
        }
        while(stop<=gas.length-1){
            rest=rest+gas[i]-cost[i];//you are at i+1 stop
            if(rest<0){
                if(i==gas.length-1){
                    i=0;
                }
                else{
                    i=i+1;
                }
                star=i;
                rest=0;
                stop=0;
            }
            else{
                if(i==gas.length-1){
                    i=0;
                }
                else{
                    i=i+1;
                }
                stop++;
            }
        }
        return star;
    }

    public static void main(String[] args) {
	int[] gas={5,1,2,3,4},cost={4,4,1,5,1};
	int res=canCompleteCircuit(gas,cost);
	System.out.println(res);
    }
}
