"""
filename: Lab_5.py
author: Tom Painadath
description: program defines a data type, which has linked list methods which can be used by clients
             to create a playlist, delete a song, Add a song at any location in the playlist, Print
             out playlist with artist name and track and playlist location
"""

import csv
import sys
import stdio
from random import sample
import random
import numpy as np

class _Node:  # Define Node class
    def __init__(self, item = None):  # Define constructor
        self.item = item  # Reference to an item
        self.next = None  # Reference to the next _Node object
        
class Playlist:  # Define Playlist class
    def __init__(self):  # Define constructor
        self._first = _Node()  # Reference to first _Node

    def push(self, item):  # Define method to push data and node
        new_node = _Node(item)  # Create a new node and pass the data
        current_node = self._first  # Set the variable current_node as the current node
        while current_node.next != None:  # Define while loop to iterate over the list while next node is not None
            current_node = current_node.next  # Set current node equal to next node
        current_node.next = new_node  # Set the last node point to the new node
        
    def size(self):  # Define method that returns the size/length of the list
        current_node = self._first  # Set the variable current_node as the current node 
        number_of_elements = 0  # initialize the variable that tracks the number of elements
        while current_node.next != None:  # Define while loop to iterate over the list while next node is not None
            number_of_elements += 1  # Increment the number of elements in the list tracker
            current_node = current_node.next  # Set current node ot next node
        return number_of_elements  # return the size of the list

    def location(self,index):  # Define method that returns the location of the 
        current_node_location = 0  # initilialize the variable current_node_location
        current_node = self._first  # Set the variable current_node as the current node 
        while True:  # Define the while loop that iterates over the list
            current_node = current_node.next  # Set current node with next node
            if current_node_location==index:   # Define if statement to check if location is found
                return current_node.item  # Return the data in the current node
            current_node_location += 1  # increment the current node location tracker by 1
            
    def delete(self,index):  # Define method that deletes a node from the list
        current_node_location = 0  # initilialize the variable current_node_location
        current_node = self._first  # Set the variable current_node as the current node
        while True:  # Define the while loop that iterates over the list
            last_node=current_node  # Set the last node to current node
            current_node=current_node.next  # Set current node with next node
            if current_node_location == index:  # Check if location is found
                last_node.next=current_node.next  # Set the node after last node to node after current node
                return  # Return from the loop
            current_node_location+=1  # Increment current node location tracker
            
    def add_item(self,index,item):  # Define method that adds a node at the given location
        if index >= self.size():  # Check if the index/location is greater than or equal to the size of the list
           return self.push(item)  # Push the node to the end of the list 
        current_node = self._first  # Set the variable current_node as the current node
        previous_node = self._first  # Set the variable previous_node as the current node
        current_node_location = 0  # initilialize the variable current_node_location
        while True:  # Define while loop that iterates over the list
            current_node = current_node.next  # Set current node with next node
            if current_node_location == index:  # Check if location to add item is found
                new_node = _Node(item)  # Create a new node and pass the data
                previous_node.next = new_node  # set node after previous node to new node
                new_node.next = current_node  # Set the node after new node to current node
                return  # exit the loop
            previous_node = current_node  # Set previous node to current node
            current_node_location += 1  # Increment the current node location tracker by one

    def str(self):  # Define method to print the list
        artist_name = []  # Initilialize artist name array
        track_name = []  # Initilialize track name array
        location = []  # Initilalize loacation array
        elements = []  # Initialize elements array
        current_node = self._first  #  Set the variable current_node as the current node
        while current_node.next != None:  # Define the while loop to iterate over the list 
            current_node = current_node.next  # Set current node to node after current node
            elements.append(current_node.item)  # Append the data in the current node to elements array
            
        for element in elements:  # Define the for loop to extract elements inside elements array of the list 
            artist_name.append(element[0])  # Append the first element in the elements array to the artist name array
            track_name.append(element[1])  # Append the second element in the elements array to the track name array
        
        i = 0  # Initialize the variable i to 0
        for i in range(len(elements)):  # Define the for loop to loop over the elements array
            print ('#' , i+1)  # Print track number or the playlist location of the track
            print('Artist name is: ', artist_name[i])  # Print the artist name
            print('Track name is: ', track_name[i])  # Print the track name
            print()  # Empty line
        i= i+1  # Increment the variable i by 1
        
###################
### Client Code ###
###################

def main():  
    num_of_tracks = int(sys.argv[1])  # Command line arguement for the number of tracks in the playlist
    delete_num = int(sys.argv[2])  # Command line arguement for the location of the track to be deleted from the playlist
    add_trackID = []  # Initialize track ID of the track to be added array
    add_trackID.append(int(sys.argv[3]))  # Append the command line arguement to the the track to be added array
    playlist = Playlist()  # Set the variable playlist with the Playlist class
    CSVpath = '/home/ec2-user/environment//Projects/LinkedList_Playlist/'  # Set the variable CDVpath to the path to the location of this file
    with open(CSVpath+'raw_tracks.csv', newline='') as csvfile:  # Opens the csv file
         tracks=csv.reader(csvfile,dialect='excel') #reads in the csv file to file tracks assuming the csv file has excel attributes
         
         i = 0  # Initialize the variable i to 0
         music = 'music'  # Set the variable music to the string 'music' as a placeholder for actual music
         random_tracks = random.sample(range(1,109728), num_of_tracks)  # Set variable random_tracks to random numbers of tracks needed to be includes in the playlist
         for row in tracks:  # For loop to interate throught each row in the CSV file
             data = row[5],row[2],row[34],row[0], music  # Set the variable data to the Artist, Album, Track name and Track ID
             if i in random_tracks:  # Check if the row number matches the random tracks number
                playlist.push(data)  # push the track data as node into the playlist
             i=i+1  # Increment the variable i by 1
    
    playlist.str()  # Print the original playlist created
      
    with open(CSVpath+'raw_tracks.csv', newline='') as csvfile:  # Opens the csv file
         tracks=csv.reader(csvfile,dialect='excel')  # Reads in the csv file to file tracks assuming the csv file has excel attributes
         
         j = 0  # Initialize the variable j to 0
         for row in tracks:  # For loop to interate throught each row in the CSV file
             new_data = row[5],row[2],row[34],row[0], music  # Set the variable data to the Artist, Album, Track name and Track ID
             if j > 0:  #Check if the current is row > 0
                 track_ID = int(row[0])  # Set the variable track_ID to the integer value of first column in the CSV file
                 if track_ID in add_trackID:  # Only print out first ten tracks for testing purposes
                    playlist.add_item(1, new_data)  # Add data to the playlist at the location specified
             j = j+1  # Increment the variable j by 1
    

    playlist.str()  # Print the playlist after the adding a song
    
    playlist.delete(delete_num-1)  # Delete a track from the playlist 

    playlist.str()  # Print the altered playlist
    

if __name__ == '__main__':
    main()
      
