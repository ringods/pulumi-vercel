// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel
{
    public static class GetEdgeConfigItem
    {
        public static Task<GetEdgeConfigItemResult> InvokeAsync(GetEdgeConfigItemArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEdgeConfigItemResult>("vercel:index/getEdgeConfigItem:getEdgeConfigItem", args ?? new GetEdgeConfigItemArgs(), options.WithDefaults());

        public static Output<GetEdgeConfigItemResult> Invoke(GetEdgeConfigItemInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEdgeConfigItemResult>("vercel:index/getEdgeConfigItem:getEdgeConfigItem", args ?? new GetEdgeConfigItemInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEdgeConfigItemArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        [Input("teamId")]
        public string? TeamId { get; set; }

        public GetEdgeConfigItemArgs()
        {
        }
        public static new GetEdgeConfigItemArgs Empty => new GetEdgeConfigItemArgs();
    }

    public sealed class GetEdgeConfigItemInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public GetEdgeConfigItemInvokeArgs()
        {
        }
        public static new GetEdgeConfigItemInvokeArgs Empty => new GetEdgeConfigItemInvokeArgs();
    }


    [OutputType]
    public sealed class GetEdgeConfigItemResult
    {
        public readonly string Id;
        public readonly string Key;
        public readonly string TeamId;
        public readonly string Value;

        [OutputConstructor]
        private GetEdgeConfigItemResult(
            string id,

            string key,

            string teamId,

            string value)
        {
            Id = id;
            Key = key;
            TeamId = teamId;
            Value = value;
        }
    }
}
