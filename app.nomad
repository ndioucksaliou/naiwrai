# Base variables
variable "AWS_ACCESS_KEY_ID" {
  type = string
}

variable "AWS_SECRET_ACCESS_KEY" {
  type = string
}

variable "AWS_DEFAULT_REGION" {
  type = string
}

variable "DOCKER_IMAGE" {
  type = string
}

variable "ENVIRONMENT" {
  type = string
}

variable "SECRETS_MANAGER_NAME" {
  type = string
}

# Deprecated
variable "docker_tag" {
  type = string
}

variable "docker_repo" {
  type = string
}

variable "git_branch" {
  type = string
}

variable "GUNICORN_WORKERS" {
  type = string
}

variable "GUNICORN_TIMEOUT" {
  type = string
}


job "newrai" {
  region = "global"
  namespace = "${var.ENVIRONMENT}"
  datacenters = ["dc1"]
  type = "service"

  update {
    stagger          = "30s"
    health_check     = "task_states"
    max_parallel     = 1
    canary           = 1
    min_healthy_time = "30s"
    healthy_deadline = "5m"
    auto_revert      = true
    auto_promote     = true
  }

  constraint {
    attribute = "${meta.type}"
    value     = "site"
  }

  group "webservice" {
    count = 1

    network {
      port "http" {
        to = 8000
      }
    }

    task "webservice" {
      driver = "docker"

      config {
        image = "${var.DOCKER_IMAGE}"
        volumes = ["/var/log/app:/var/log/app"]
        ports = ["http"]
      }

      service {
        port = "http"
        provider = "nomad"
        tags = [
          "traefik.enable=true",
          "traefik.http.routers.newrai.rule=Host(`newrai.${var.ENVIRONMENT}.neonumy.dev`)",
        ]

        check {
          type     = "tcp"
          interval = "60s"
          timeout  = "30s"

          check_restart {
            limit = 3
            grace = "30s"
            ignore_warnings = false
          }
        }
      }

      env {
        AWS_DEFAULT_REGION     = "${var.AWS_DEFAULT_REGION}"
        AWS_SECRET_ACCESS_KEY  = "${var.AWS_SECRET_ACCESS_KEY}"
        AWS_ACCESS_KEY_ID      = "${var.AWS_ACCESS_KEY_ID}"

        ENVIRONMENT            = "${var.ENVIRONMENT}"
        SECRETS_MANAGER_NAME   = "${var.SECRETS_MANAGER_NAME}"
        DJANGO_SETTINGS_MODULE = "app.settings.${var.ENVIRONMENT}"
      }

      resources {
        cpu    = 450 # MHz
        memory = 330 # MB
      }
    }
  }
}

