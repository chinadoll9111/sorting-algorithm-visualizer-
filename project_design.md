 project_design.md
                ┌───────────────┐
                │      USER     │
                └───────┬───────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │        GUI INTERFACE              │
        │ (Tkinter / Pygame)                │
        │-----------------------------------│
        │ • Select Algorithm                │
        │ • Generate Array                  │
        │ • Start / Reset                   │
        │ • Adjust Speed                    │
        │ • Display Bars (Canvas)           │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │           CONTROLLER              │
        │-----------------------------------│
        │ • start_sort()                    │
        │ • reset_array()                   │
        │ • set_speed()                     │
        │ • handle_user_input()             │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │     SORTING ALGORITHM ENGINE      │
        │-----------------------------------│
        │ • bubble_sort()                   │
        │ • selection_sort()                │
        │ • insertion_sort()                │
        │ • merge_sort()                    │
        │ • quick_sort()                    │
        │                                   │
        │ Outputs operations like:          │
        │ (compare, i, j)                   │
        │ (swap, i, j)                      │
        │ (overwrite, index, value)         │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │        ANIMATION RENDERER         │
        │-----------------------------------│
        │ • Reads operation steps           │
        │ • Updates bar heights             │
        │ • Changes bar colors              │
        │   (compare / swap / sorted)       │
        │ • Controls animation speed        │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │   UPDATED VISUALIZATION ON GUI    │
        │-----------------------------------│
        │ → Compared bars highlighted       │
        │ → Swapped bars updated            │
        │ → Sorted bars marked              │
        └───────────────┬───────────────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Is Array Sorted?│
                └───────┬────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
          NO                        YES
           │                         │
           ▼                         ▼
   Repeat Compare & Swap        END PROCESS
        (Loop Back to
   Sorting Algorithm Engine)

   Sorting Algorithm Engine)
