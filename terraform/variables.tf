variable "generic" {
  description = "general values for project"
  type = object({
    policy_prefix = string
    role_prefix   = string
    project_name  = string
  })
}

variable "cloudfront" {
  description = "value of cloudfront"
  type = object({
    default_root_object = string
    custom_error_responses = list(object({
      error_caching_min_ttl = number
      error_code            = number
      response_code         = number
      response_page_path    = string
    }))
    comment = string
    aliases = list(string)
    default_cache_behavior = object({
      cache_policy_id = object({
        CachingDisabled                        = string
        CachingOptimized                       = string
        CachingOptimizedForUncompressedObjects = string
        Elemental-MediaPackage                 = string
      })
      viewer_protocol_policy = string
      allowed_methods        = list(string)
      cached_methods         = list(string)
    })
    price_class = string
    restrictions = object({
      geo_restriction = object({
        restriction_type = string
        locations        = list(string)
      })
    })
    viewer_certificate = object({
      cloudfront_default_certificate = bool
    })
  })
}
