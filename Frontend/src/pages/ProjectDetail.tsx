import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Navbar } from "@/components/ui/navbar";
import { Plus, Users, Calendar, MessageSquare, Paperclip, MoreHorizontal } from "lucide-react";
import { useParams, Link } from "react-router-dom";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";

const ProjectDetail = () => {
  const { id } = useParams();
  const user = {
    name: "John Doe",
    email: "john@example.com",
    avatar: "/placeholder.svg"
  };

  const [tasks, setTasks] = useState({
    todo: [
      {
        id: 1,
        title: "Design homepage wireframes",
        description: "Create wireframes for the new homepage layout",
        assignee: "Sarah Johnson",
        priority: "High",
        dueDate: "2024-01-25",
        comments: 3,
        attachments: 2
      },
      {
        id: 2,
        title: "Set up development environment",
        description: "Configure local development setup with Docker",
        assignee: "Mike Chen",
        priority: "Medium",
        dueDate: "2024-01-22",
        comments: 1,
        attachments: 0
      }
    ],
    inProgress: [
      {
        id: 3,
        title: "Implement user authentication",
        description: "Build login/register functionality with JWT",
        assignee: "John Doe",
        priority: "High",
        dueDate: "2024-01-28",
        comments: 5,
        attachments: 1
      },
      {
        id: 4,
        title: "Create API endpoints",
        description: "Develop RESTful API for user management",
        assignee: "Lisa Wang",
        priority: "Medium",
        dueDate: "2024-01-30",
        comments: 2,
        attachments: 3
      }
    ],
    review: [
      {
        id: 5,
        title: "Database schema design",
        description: "Design and review database schema for user data",
        assignee: "David Brown",
        priority: "High",
        dueDate: "2024-01-20",
        comments: 8,
        attachments: 1
      }
    ],
    done: [
      {
        id: 6,
        title: "Project setup and initialization",
        description: "Initialize project repository and basic structure",
        assignee: "John Doe",
        priority: "Low",
        dueDate: "2024-01-15",
        comments: 2,
        attachments: 0
      },
      {
        id: 7,
        title: "Requirements gathering",
        description: "Collect and document project requirements",
        assignee: "Sarah Johnson",
        priority: "Medium",
        dueDate: "2024-01-18",
        comments: 12,
        attachments: 5
      }
    ]
  });

  const columns = [
    { id: 'todo', title: 'To Do', color: 'bg-muted', tasks: tasks.todo },
    { id: 'inProgress', title: 'In Progress', color: 'bg-primary/10', tasks: tasks.inProgress },
    { id: 'review', title: 'Review', color: 'bg-warning/10', tasks: tasks.review },
    { id: 'done', title: 'Done', color: 'bg-success/10', tasks: tasks.done }
  ];

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'High': return 'bg-destructive/10 text-destructive';
      case 'Medium': return 'bg-warning/10 text-warning';
      case 'Low': return 'bg-success/10 text-success';
      default: return 'bg-muted text-muted-foreground';
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar user={user} />
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <div className="flex items-center space-x-2 mb-2">
              <Link to="/projects" className="text-muted-foreground hover:text-foreground">
                Projects
              </Link>
              <span className="text-muted-foreground">/</span>
              <span className="text-foreground">Website Redesign</span>
            </div>
            <h1 className="text-3xl font-bold text-foreground">Website Redesign</h1>
            <p className="text-muted-foreground mt-1">Complete overhaul of company website</p>
          </div>
          <div className="flex items-center space-x-3">
            <Button variant="outline">
              <Users className="w-4 h-4 mr-2" />
              Invite Team
            </Button>
            <Button variant="hero">
              <Plus className="w-4 h-4 mr-2" />
              Add Task
            </Button>
          </div>
        </div>

        {/* Kanban Board */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {columns.map((column) => (
            <div key={column.id} className="flex flex-col">
              {/* Column Header */}
              <div className={`rounded-lg p-4 mb-4 ${column.color}`}>
                <div className="flex items-center justify-between">
                  <h3 className="font-semibold text-foreground">{column.title}</h3>
                  <Badge variant="secondary" className="ml-2">
                    {column.tasks.length}
                  </Badge>
                </div>
              </div>

              {/* Tasks */}
              <div className="space-y-3 flex-1">
                {column.tasks.map((task) => (
                  <Card key={task.id} className="bg-gradient-card border-0 hover:shadow-md transition-all duration-200 cursor-pointer group">
                    <CardHeader className="pb-3">
                      <div className="flex items-start justify-between">
                        <CardTitle className="text-sm font-medium text-foreground line-clamp-2">
                          {task.title}
                        </CardTitle>
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <Button variant="ghost" size="sm" className="opacity-0 group-hover:opacity-100 transition-opacity w-6 h-6 p-0">
                              <MoreHorizontal className="w-3 h-3" />
                            </Button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align="end">
                            <DropdownMenuItem>Edit Task</DropdownMenuItem>
                            <DropdownMenuItem>Move to...</DropdownMenuItem>
                            <DropdownMenuItem>Delete</DropdownMenuItem>
                          </DropdownMenuContent>
                        </DropdownMenu>
                      </div>
                      {task.description && (
                        <p className="text-xs text-muted-foreground line-clamp-2">
                          {task.description}
                        </p>
                      )}
                    </CardHeader>
                    
                    <CardContent className="pt-0">
                      <div className="space-y-3">
                        {/* Priority & Due Date */}
                        <div className="flex items-center justify-between">
                          <Badge variant="outline" className={`text-xs ${getPriorityColor(task.priority)}`}>
                            {task.priority}
                          </Badge>
                          <div className="flex items-center text-xs text-muted-foreground">
                            <Calendar className="w-3 h-3 mr-1" />
                            {new Date(task.dueDate).toLocaleDateString()}
                          </div>
                        </div>

                        {/* Assignee */}
                        <div className="flex items-center text-xs text-muted-foreground">
                          <Users className="w-3 h-3 mr-1" />
                          {task.assignee}
                        </div>

                        {/* Comments & Attachments */}
                        <div className="flex items-center justify-between text-xs text-muted-foreground">
                          <div className="flex items-center">
                            <MessageSquare className="w-3 h-3 mr-1" />
                            {task.comments}
                          </div>
                          {task.attachments > 0 && (
                            <div className="flex items-center">
                              <Paperclip className="w-3 h-3 mr-1" />
                              {task.attachments}
                            </div>
                          )}
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                ))}
                
                {/* Add Task Button */}
                <Button 
                  variant="ghost" 
                  className="w-full h-12 border-2 border-dashed border-muted-foreground/20 hover:border-primary/50 hover:bg-primary/5"
                >
                  <Plus className="w-4 h-4 mr-2" />
                  Add Task
                </Button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ProjectDetail;