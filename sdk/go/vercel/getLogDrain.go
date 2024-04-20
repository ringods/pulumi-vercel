// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

// Provides information about an existing Log Drain.
//
// Log Drains collect all of your logs using a service specializing in storing app logs.
//
// Teams on Pro and Enterprise plans can subscribe to log drains that are generic and configurable from the Vercel dashboard without creating an integration. This allows you to use a HTTP service to receive logs through Vercel's log drains.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := vercel.LookupLogDrain(ctx, &vercel.LookupLogDrainArgs{
//				Id: "lg_xxxxxxx_xxxxxx_xxxxx",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
func LookupLogDrain(ctx *pulumi.Context, args *LookupLogDrainArgs, opts ...pulumi.InvokeOption) (*LookupLogDrainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLogDrainResult
	err := ctx.Invoke("vercel:index/getLogDrain:getLogDrain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLogDrain.
type LookupLogDrainArgs struct {
	// Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpointVerification data source. The value the `x-vercel-verify` header should be can be read from the `vercelEndpointVerificationCode` data source.
	Endpoint string `pulumi:"endpoint"`
	// The ID of the Log Drain.
	Id string `pulumi:"id"`
	// The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId *string `pulumi:"teamId"`
}

// A collection of values returned by getLogDrain.
type LookupLogDrainResult struct {
	// The format log data should be delivered in. Can be `json` or `ndjson`.
	DeliveryFormat string `pulumi:"deliveryFormat"`
	// Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpointVerification data source. The value the `x-vercel-verify` header should be can be read from the `vercelEndpointVerificationCode` data source.
	Endpoint string `pulumi:"endpoint"`
	// Logs from the selected environments will be forwarded to your webhook. At least one must be present.
	Environments []string `pulumi:"environments"`
	// Custom headers to include in requests to the log drain endpoint.
	Headers map[string]string `pulumi:"headers"`
	// The ID of the Log Drain.
	Id string `pulumi:"id"`
	// A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
	ProjectIds []string `pulumi:"projectIds"`
	// A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
	SamplingRate float64 `pulumi:"samplingRate"`
	// A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `function`.
	Sources []string `pulumi:"sources"`
	// The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId string `pulumi:"teamId"`
}

func LookupLogDrainOutput(ctx *pulumi.Context, args LookupLogDrainOutputArgs, opts ...pulumi.InvokeOption) LookupLogDrainResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLogDrainResult, error) {
			args := v.(LookupLogDrainArgs)
			r, err := LookupLogDrain(ctx, &args, opts...)
			var s LookupLogDrainResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLogDrainResultOutput)
}

// A collection of arguments for invoking getLogDrain.
type LookupLogDrainOutputArgs struct {
	// Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpointVerification data source. The value the `x-vercel-verify` header should be can be read from the `vercelEndpointVerificationCode` data source.
	Endpoint pulumi.StringInput `pulumi:"endpoint"`
	// The ID of the Log Drain.
	Id pulumi.StringInput `pulumi:"id"`
	// The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringPtrInput `pulumi:"teamId"`
}

func (LookupLogDrainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogDrainArgs)(nil)).Elem()
}

// A collection of values returned by getLogDrain.
type LookupLogDrainResultOutput struct{ *pulumi.OutputState }

func (LookupLogDrainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogDrainResult)(nil)).Elem()
}

func (o LookupLogDrainResultOutput) ToLookupLogDrainResultOutput() LookupLogDrainResultOutput {
	return o
}

func (o LookupLogDrainResultOutput) ToLookupLogDrainResultOutputWithContext(ctx context.Context) LookupLogDrainResultOutput {
	return o
}

// The format log data should be delivered in. Can be `json` or `ndjson`.
func (o LookupLogDrainResultOutput) DeliveryFormat() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogDrainResult) string { return v.DeliveryFormat }).(pulumi.StringOutput)
}

// Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpointVerification data source. The value the `x-vercel-verify` header should be can be read from the `vercelEndpointVerificationCode` data source.
func (o LookupLogDrainResultOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogDrainResult) string { return v.Endpoint }).(pulumi.StringOutput)
}

// Logs from the selected environments will be forwarded to your webhook. At least one must be present.
func (o LookupLogDrainResultOutput) Environments() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLogDrainResult) []string { return v.Environments }).(pulumi.StringArrayOutput)
}

// Custom headers to include in requests to the log drain endpoint.
func (o LookupLogDrainResultOutput) Headers() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupLogDrainResult) map[string]string { return v.Headers }).(pulumi.StringMapOutput)
}

// The ID of the Log Drain.
func (o LookupLogDrainResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogDrainResult) string { return v.Id }).(pulumi.StringOutput)
}

// A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
func (o LookupLogDrainResultOutput) ProjectIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLogDrainResult) []string { return v.ProjectIds }).(pulumi.StringArrayOutput)
}

// A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
func (o LookupLogDrainResultOutput) SamplingRate() pulumi.Float64Output {
	return o.ApplyT(func(v LookupLogDrainResult) float64 { return v.SamplingRate }).(pulumi.Float64Output)
}

// A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `function`.
func (o LookupLogDrainResultOutput) Sources() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLogDrainResult) []string { return v.Sources }).(pulumi.StringArrayOutput)
}

// The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
func (o LookupLogDrainResultOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogDrainResult) string { return v.TeamId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLogDrainResultOutput{})
}
