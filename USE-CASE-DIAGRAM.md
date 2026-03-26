# Use Case Diagram: Smart Campus Connect

## Diagram

```mermaid
graph TD
    subgraph Actors
        Student[Student]
        Faculty[Faculty Member]
        Admin[Administrator]
        ITStaff[IT Staff]
        Parent[Parent]
        Security[Campus Security]
    end
    
    subgraph System Boundary
        subgraph Academic Module
            UC1[View Grades]
            UC2[Submit Assignment]
            UC3[Take Attendance]
            UC4[Create Assignment]
        end
        
        subgraph Campus Module
            UC5[Find Study Space]
            UC6[Track Shuttle]
            UC7[View Campus Map]
        end
        
        subgraph Event Module
            UC8[Create Event]
            UC9[Register for Event]
            UC10[Approve Event]
        end
        
        subgraph Social Module
            UC11[Create Study Group]
            UC12[Send Message]
        end
        
        subgraph Other Module
            UC13[View Meal Plan]
            UC14[Report Lost Item]
            UC15[Send Emergency Alert]
        end
    end
    
    Student --> UC1
    Student --> UC2
    Student --> UC5
    Student --> UC6
    Student --> UC7
    Student --> UC9
    Student --> UC11
    Student --> UC12
    Student --> UC13
    Student --> UC14
    
    Faculty --> UC3
    Faculty --> UC4
    Faculty --> UC1
    Faculty --> UC8
    
    Admin --> UC10
    Admin --> UC15
    Admin --> UC5
    
    Security --> UC15
    Security --> UC5
    
    Parent --> UC13
    
    UC8 -.->|<<includes>>| UC9
    UC11 -.->|<<includes>>| UC12
