import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Navbar } from "@/components/ui/navbar";
import { Plus, Users, Calendar, MoreHorizontal, TrendingUp } from "lucide-react";
import { Link } from "react-router-dom";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";

const Projects = () => {
  const user = {
    name: "John Doe",
    email: "john@example.com",
    avatar: "/placeholder.svg"
  };

  const projects = [
    {
      id: 1,
      name: "Website Redesign",
      description: "Complete overhaul of company website with modern design and improved UX",
      progress: 75,
      dueDate: "Feb 15, 2024",
      status: "In Progress",
      priority: "High",
      members: 5,
      tasks: { total: 24, completed: 18 },
      color: "bg-primary"
    },
    {
      id: 2,
      name: "Mobile App Development",
      description: "iOS and Android app for customer portal with real-time features",
      progress: 45,
      dueDate: "Mar 1, 2024",
      status: "In Progress",
      priority: "High",
      members: 3,
      tasks: { total: 32, completed: 14 },
      color: "bg-secondary"
    },
    {
      id: 3,
      name: "Marketing Campaign",
      description: "Q1 marketing campaign planning and execution across all channels",
      progress: 90,
      dueDate: "Jan 30, 2024",
      status: "Review",
      priority: "Medium",
      members: 4,
      tasks: { total: 16, completed: 14 },
      color: "bg-success"
    },
    {
      id: 4,
      name: "Database Migration",
      description: "Migrate legacy database to new cloud infrastructure",
      progress: 30,
      dueDate: "Apr 15, 2024",
      status: "Planning",
      priority: "Medium",
      members: 2,
      tasks: { total: 28, completed: 8 },
      color: "bg-warning"
    },
    {
      id: 5,
      name: "API Integration",
      description: "Integrate third-party APIs for enhanced functionality",
      progress: 60,
      dueDate: "Mar 10, 2024",
      status: "In Progress",
      priority: "Low",
      members: 3,
      tasks: { total: 20, completed: 12 },
      color: "bg-accent"
    },
    {
      id: 6,
      name: "Security Audit",
      description: "Comprehensive security audit and vulnerability assessment",
      progress: 25,
      dueDate: "May 1, 2024",
      status: "Planning",
      priority: "High",
      members: 4,
      tasks: { total: 35, completed: 9 },
      color: "bg-destructive"
    }
  ];

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'High': return 'bg-destructive/10 text-destructive';
      case 'Medium': return 'bg-warning/10 text-warning';
      case 'Low': return 'bg-success/10 text-success';
      default: return 'bg-muted text-muted-foreground';
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'In Progress': return 'bg-primary/10 text-primary';
      case 'Review': return 'bg-warning/10 text-warning';
      case 'Planning': return 'bg-muted text-muted-foreground';
      case 'Completed': return 'bg-success/10 text-success';
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
            <h1 className="text-3xl font-bold text-foreground">Projects</h1>
            <p className="text-muted-foreground mt-1">Manage and track your team's projects</p>
          </div>
          <Button variant="hero" asChild>
            <Link to="/projects/new">
              <Plus className="w-4 h-4 mr-2" />
              New Project
            </Link>
          </Button>
        </div>

        {/* Projects Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project) => (
            <Card key={project.id} className="bg-gradient-card border-0 hover:shadow-lg transition-all duration-300 group">
              <CardHeader className="pb-3">
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center space-x-2 mb-2">
                      <div className={`w-3 h-3 rounded-full ${project.color}`}></div>
                      <CardTitle className="text-lg">{project.name}</CardTitle>
                    </div>
                    <div className="flex items-center space-x-2 mb-3">
                      <Badge variant="secondary" className={getStatusColor(project.status)}>
                        {project.status}
                      </Badge>
                      <Badge variant="outline" className={getPriorityColor(project.priority)}>
                        {project.priority}
                      </Badge>
                    </div>
                  </div>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="sm" className="opacity-0 group-hover:opacity-100 transition-opacity">
                        <MoreHorizontal className="w-4 h-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuItem>Edit Project</DropdownMenuItem>
                      <DropdownMenuItem>View Details</DropdownMenuItem>
                      <DropdownMenuItem>Archive</DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </div>
                <CardDescription className="text-sm line-clamp-2">
                  {project.description}
                </CardDescription>
              </CardHeader>
              
              <CardContent className="pt-0">
                <div className="space-y-4">
                  {/* Progress */}
                  <div>
                    <div className="flex items-center justify-between text-sm mb-2">
                      <span className="text-muted-foreground">Progress</span>
                      <span className="font-medium text-foreground">{project.progress}%</span>
                    </div>
                    <div className="w-full bg-muted rounded-full h-2">
                      <div 
                        className="bg-gradient-primary h-2 rounded-full transition-all duration-300" 
                        style={{ width: `${project.progress}%` }}
                      ></div>
                    </div>
                  </div>

                  {/* Stats */}
                  <div className="flex items-center justify-between text-xs text-muted-foreground">
                    <div className="flex items-center">
                      <Users className="w-3 h-3 mr-1" />
                      {project.members} members
                    </div>
                    <div className="flex items-center">
                      <Calendar className="w-3 h-3 mr-1" />
                      Due {project.dueDate}
                    </div>
                  </div>

                  {/* Tasks */}
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-muted-foreground">
                      {project.tasks.completed}/{project.tasks.total} tasks completed
                    </span>
                    <div className="flex items-center text-success">
                      <TrendingUp className="w-3 h-3 mr-1" />
                      On track
                    </div>
                  </div>

                  {/* Action Button */}
                  <Button variant="outline" className="w-full mt-4" asChild>
                    <Link to={`/projects/${project.id}`}>
                      View Project
                    </Link>
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Empty State for when no projects exist */}
        {projects.length === 0 && (
          <Card className="bg-gradient-card border-0 text-center py-12">
            <CardContent>
              <div className="w-16 h-16 bg-gradient-primary rounded-xl flex items-center justify-center mx-auto mb-4">
                <Plus className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">No projects yet</h3>
              <p className="text-muted-foreground mb-6">Get started by creating your first project</p>
              <Button variant="hero" asChild>
                <Link to="/projects/new">Create Your First Project</Link>
              </Button>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
};

export default Projects;