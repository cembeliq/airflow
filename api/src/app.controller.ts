import { Body, Controller, Get, Post } from '@nestjs/common';
import { AppService } from './app.service';

interface ProcessedData {
  processed: boolean;
  timestamp: string | null;
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Post('api/data')
  async processData(@Body() data: ProcessedData) {
    console.log('Received data:', data);
    return { success: true, receivedData: data };
  }
}
