# Cigarette-Smokers-Problem
My solution for the classical operating system related synchronization problem, the Cigarette Smokers' Problem, part of the Complex Engineering Problem of the 6th semester Operating System Course at NED University.

# Problem Description
### The Cigarette smokers’ problem
Four threads are involved: an agent and three smokers. The smokers loop forever, first waiting for ingredients,
then making and smoking cigarettes. The ingredients are tobacco, paper, and matches. We assume that the agent
has an infinite supply of all three ingredients, and each smoker has an infinite supply of one of the ingredients;
that is, one smoker has matches, another has paper, and the third has tobacco.
The agent repeatedly chooses two different ingredients at random and makes them available to the smokers.
Depending on which ingredients are chosen, the smoker with the complementary ingredient should pick up both
resources and proceed. For example, if the agent puts out tobacco and paper, the smoker with the matches should
pick up both ingredients, make a cigarette, and then signal the agent. To explain the premise, the agent represents
an operating system that allocates resources, and the smokers represent applications that need resources.
The problem is to make sure that if resources are available that would allow one or more applications to proceed,
those applications should be woken up. Conversely, we want to avoid waking an application if it cannot proceed.
The restriction imposed on the system is you are not allowed to modify the agent code. If the agent represents an
operating system, it makes sense to assume that you don’t want to modify it every time a new application comes
along. So the abilities of the agent remain as defined in the problem.
