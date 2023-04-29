#include <stdio.h>
#include <stdbool.h>
#include <unistd.h> 

#define NUM_FLOORS 5

// Elevator status
typedef struct {
  int current_floor;
  bool door_open;
  bool moving_up;
} elevator_t;

// Initialize the elevator to the first floor with the door closed
void elevator_init(elevator_t *elevator) {
  elevator->current_floor = 1;
  elevator->door_open = false;
  elevator->moving_up = true;
}

// Move the elevator up one floor
void elevator_move_up(elevator_t *elevator) {
  elevator->current_floor++;
}

// Move the elevator down one floor
void elevator_move_down(elevator_t *elevator) {
  elevator->current_floor--;
}

// Open the elevator door
void elevator_open_door(elevator_t *elevator) {
  elevator->door_open = true;
}

// Close the elevator door
void elevator_close_door(elevator_t *elevator) {
  elevator->door_open = false;
}

// Print the current status of the elevator
void elevator_print_status(elevator_t *elevator) {
  printf("Floor %d - Door %s - %s\n",
         elevator->current_floor,
         elevator->door_open ? "Open" : "Closed",
         elevator->moving_up ? "Going Up" : "Going Down");
}

// Main function
int main() {
  elevator_t elevator;
  elevator_init(&elevator);

  while (true) {
    // Print the current status of the elevator
    elevator_print_status(&elevator);

    // Wait for user input
    printf("Select a floor (1-%d): ", NUM_FLOORS);
    int selected_floor;
    scanf("%d", &selected_floor);

    // Move the elevator to the selected floor
    while (elevator.current_floor != selected_floor) {
      if (elevator.current_floor < selected_floor) {
        elevator.moving_up = true;
        elevator_move_up(&elevator);
      } else {
        elevator.moving_up = false;
        elevator_move_down(&elevator);
      }
    }

    // Open the elevator door
    elevator_open_door(&elevator);

    // Wait for a few seconds
    printf("Door opening...\n");
    for (int i = 0; i < 5; i++) {
      printf("%d...\n", 5 - i);
      sleep(1);
    }

    // Close the elevator door
    elevator_close_door(&elevator);
    printf("Door closed.\n");
  }

  return 0;
}
